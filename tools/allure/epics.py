from enum import Enum


class AllureEpic(str, Enum):
    LMS = "LMS system"
    STUDENTS = "STUDENTS system"
    ADMINISTRATION = "ADMINISTRATION system"