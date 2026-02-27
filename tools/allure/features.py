from enum import Enum


class AllureFeature(str, Enum):
    DASHBOARD = "Dashboard"
    COURSES = "Courses"
    AUTHENTICATION = "Authentication"