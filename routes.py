from flask import Blueprint, jsonify, request
from dtos import PacienteCreateDTO, PacienteDTO, EstatisticasDTO
from models import Paciente

api = Blueprint("api", __name__)


@api.route("/", methods=["GET"])
def home():
    """
    Informação da API
    ---
    tags:
      - Geral
    responses:
      200:
        description: Status da API
        schema:
          type: object
          properties:
            mensagem:
              type: string
            status:
              type: string
    """
    return jsonify({
        "mensagem": "BeautyFlow API",
        "status": "Online"
    })


@api.route("/pacientes", methods=["GET"])
def listar_pacientes():
    """
    Lista todos os pacientes
    ---
    tags:
      - Pacientes
    responses:
      200:
        description: Lista de pacientes
    """

    return jsonify([PacienteDTO.from_dict(p).to_dict() for p in Paciente.listar()])


@api.route("/pacientes/<int:id>", methods=["GET"])
def buscar_paciente(id):
        """
        Busca um paciente pelo ID
        ---
        tags:
            - Pacientes
        parameters:
            - name: id
              in: path
              description: ID do paciente
              required: true
              type: integer
        responses:
            200:
                description: Dados do paciente
            404:
                description: Paciente não encontrado
        """

        paciente = Paciente.buscar(id)

        if paciente is None:
                return jsonify({"erro": "Paciente não encontrado"}), 404

        return jsonify(PacienteDTO.from_dict(paciente).to_dict())


@api.route("/pacientes", methods=["POST"])
def cadastrar():

        """
        Cadastra um paciente
        ---
        tags:
            - Pacientes
        consumes:
            - application/json
        produces:
            - application/json
        parameters:
            - in: body
              name: paciente
              description: Dados do paciente
              required: true
              schema:
                type: object
                required:
                    - nome
                    - idade
                    - telefone
                    - email
                    - tipo_pele
                    - queixa_principal
                properties:
                    nome:
                        type: string
                    idade:
                        type: integer
                    telefone:
                        type: string
                    email:
                        type: string
                    tipo_pele:
                        type: string
                    queixa_principal:
                        type: string
        responses:
            201:
                description: Paciente cadastrado com sucesso
            400:
                description: Campos obrigatórios ausentes
        """

        dados = request.get_json() or {}
        paciente_dto = PacienteCreateDTO.from_dict(dados)

        if not paciente_dto.nome or not paciente_dto.idade or not paciente_dto.telefone or not paciente_dto.email or not paciente_dto.tipo_pele or not paciente_dto.queixa_principal:
            return jsonify({
                "erro": "Todos os campos obrigatórios devem ser preenchidos."
            }), 400

        Paciente.cadastrar(paciente_dto)

        return jsonify({
                "mensagem": "Paciente cadastrado com sucesso."
        }), 201


@api.route("/pacientes/<int:id>", methods=["PUT"])
def atualizar(id):

    """
    Atualiza um paciente pelo ID
    ---
    tags:
        - Pacientes
    consumes:
        - application/json
    produces:
        - application/json
    parameters:
        - name: id
          in: path
          description: ID do paciente
          required: true
          type: integer
        - in: body
          name: paciente
          description: Dados atualizados do paciente
          required: true
          schema:
            type: object
            properties:
                nome:
                    type: string
                idade:
                    type: integer
                telefone:
                    type: string
                email:
                    type: string
                tipo_pele:
                    type: string
                queixa_principal:
                    type: string
    responses:
        200:
            description: Paciente atualizado.
        404:
            description: Paciente não encontrado.
    """

    paciente = Paciente.buscar(id)

    if paciente is None:
        return jsonify({
            "erro": "Paciente não encontrado."
        }), 404

    dados = request.get_json() or {}
    paciente_dto = PacienteCreateDTO.from_dict(dados)

    if not paciente_dto.nome or not paciente_dto.idade or not paciente_dto.telefone or not paciente_dto.email or not paciente_dto.tipo_pele or not paciente_dto.queixa_principal:
        return jsonify({
            "erro": "Todos os campos obrigatórios devem ser preenchidos."
        }), 400

    Paciente.atualizar(id, paciente_dto)

    return jsonify({
        "mensagem": "Paciente atualizado."
    })


@api.route("/pacientes/<int:id>", methods=["DELETE"])
def excluir(id):

    """
    Remove um paciente pelo ID
    ---
    tags:
        - Pacientes
    parameters:
        - name: id
          in: path
          description: ID do paciente
          required: true
          type: integer
    responses:
        200:
            description: Paciente removido.
        404:
            description: Paciente não encontrado.
    """

    paciente = Paciente.buscar(id)

    if paciente is None:
        return jsonify({
            "erro": "Paciente não encontrado."
        }), 404

    Paciente.excluir(id)

    return jsonify({
        "mensagem": "Paciente removido."
    })


@api.route("/estatisticas", methods=["GET"])
def estatisticas():

    """
    Retorna e grava estatísticas de pacientes
    ---
    tags:
        - Pacientes
    responses:
        200:
            description: Estatísticas de pacientes calculadas e persistidas
            schema:
                type: object
                properties:
                    total_pacientes:
                        type: integer
                    pele_oleosa:
                        type: integer
                    pele_seca:
                        type: integer
                    pele_mista:
                        type: integer
                    pele_normal:
                        type: integer
    """

    return jsonify(EstatisticasDTO.from_dict(Paciente.estatisticas()).to_dict())
