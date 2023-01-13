from pydantic import Field
from . import BaseDTO


class GroupDTO(BaseDTO):
    groupId: str = Field(alias="group_id")
    IsReportAgree: bool = Field(alias="is_report_agree")
