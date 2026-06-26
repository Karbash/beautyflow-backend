from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any, Dict, Optional


@dataclass
class PacienteCreateDTO:
    nome: str
    idade: int
    telefone: str
    email: str
    tipo_pele: str
    queixa_principal: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PacienteCreateDTO":
        return cls(
            nome=str(data.get("nome", "") or "").strip(),
            idade=int(data.get("idade") or 0),
            telefone=str(data.get("telefone", "") or "").strip(),
            email=str(data.get("email", "") or "").strip(),
            tipo_pele=str(data.get("tipo_pele", "") or "").strip(),
            queixa_principal=str(data.get("queixa_principal", "") or "").strip(),
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class PacienteDTO(PacienteCreateDTO):
    id: Optional[int] = None
    data_cadastro: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PacienteDTO":
        return cls(
            id=data.get("id"),
            nome=str(data.get("nome", "") or "").strip(),
            idade=int(data.get("idade") or 0),
            telefone=str(data.get("telefone", "") or "").strip(),
            email=str(data.get("email", "") or "").strip(),
            tipo_pele=str(data.get("tipo_pele", "") or "").strip(),
            queixa_principal=str(data.get("queixa_principal", "") or "").strip(),
            data_cadastro=data.get("data_cadastro"),
        )


@dataclass
class EstatisticasDTO:
    total_pacientes: int
    pele_oleosa: int
    pele_seca: int
    pele_mista: int
    pele_normal: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "EstatisticasDTO":
        return cls(
            total_pacientes=int(data.get("total_pacientes") or 0),
            pele_oleosa=int(data.get("pele_oleosa") or 0),
            pele_seca=int(data.get("pele_seca") or 0),
            pele_mista=int(data.get("pele_mista") or 0),
            pele_normal=int(data.get("pele_normal") or 0),
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
