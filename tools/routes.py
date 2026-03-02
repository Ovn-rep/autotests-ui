from enum import StrEnum


class AppRoute(StrEnum):
    LOGIN = "./#/auth/login"
    REGISTRATION = "./#/auth/registration"

    DASHBOARD = "./#/dashboard"

    COURSES = "./#/courses"
    COURSES_CREATE = "./#/courses/create"