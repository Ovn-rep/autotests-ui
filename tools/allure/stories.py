from enum import Enum


class AllureStory(str, Enum):
    DASHBOARD = "Dashboard"
    COURSES = "Courses"
    REGISTRATION = "Registration"
    AUTHORIZATION = "Authorization"