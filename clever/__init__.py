# coding: utf-8

# flake8: noqa

"""
    Clever API

    The Clever API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from clever.api.data_api import DataApi
from clever.api.events_api import EventsApi
# import ApiClient
from clever.api_client import ApiClient
from clever.configuration import Configuration
# import models into sdk package
from clever.models.bad_request import BadRequest
from clever.models.contact import Contact
from clever.models.course import Course
from clever.models.course_object import CourseObject
from clever.models.course_response import CourseResponse
from clever.models.courses_created import CoursesCreated
from clever.models.courses_deleted import CoursesDeleted
from clever.models.courses_response import CoursesResponse
from clever.models.courses_updated import CoursesUpdated
from clever.models.credentials import Credentials
from clever.models.district import District
from clever.models.district_admin import DistrictAdmin
from clever.models.district_contact import DistrictContact
from clever.models.district_object import DistrictObject
from clever.models.district_response import DistrictResponse
from clever.models.districts_created import DistrictsCreated
from clever.models.districts_deleted import DistrictsDeleted
from clever.models.districts_response import DistrictsResponse
from clever.models.districts_updated import DistrictsUpdated
from clever.models.event import Event
from clever.models.event_response import EventResponse
from clever.models.events_response import EventsResponse
from clever.models.internal_error import InternalError
from clever.models.link import Link
from clever.models.location import Location
from clever.models.name import Name
from clever.models.not_found import NotFound
from clever.models.principal import Principal
from clever.models.resource import Resource
from clever.models.resource_object import ResourceObject
from clever.models.resource_response import ResourceResponse
from clever.models.resources_created import ResourcesCreated
from clever.models.resources_deleted import ResourcesDeleted
from clever.models.resources_response import ResourcesResponse
from clever.models.resources_updated import ResourcesUpdated
from clever.models.roles import Roles
from clever.models.school import School
from clever.models.school_enrollment import SchoolEnrollment
from clever.models.school_object import SchoolObject
from clever.models.school_response import SchoolResponse
from clever.models.schools_created import SchoolsCreated
from clever.models.schools_deleted import SchoolsDeleted
from clever.models.schools_response import SchoolsResponse
from clever.models.schools_updated import SchoolsUpdated
from clever.models.section import Section
from clever.models.section_object import SectionObject
from clever.models.section_response import SectionResponse
from clever.models.sections_created import SectionsCreated
from clever.models.sections_deleted import SectionsDeleted
from clever.models.sections_response import SectionsResponse
from clever.models.sections_updated import SectionsUpdated
from clever.models.staff import Staff
from clever.models.student import Student
from clever.models.student_relationship import StudentRelationship
from clever.models.teacher import Teacher
from clever.models.term import Term
from clever.models.term_object import TermObject
from clever.models.term_response import TermResponse
from clever.models.terms_created import TermsCreated
from clever.models.terms_deleted import TermsDeleted
from clever.models.terms_response import TermsResponse
from clever.models.terms_updated import TermsUpdated
from clever.models.user import User
from clever.models.user_object import UserObject
from clever.models.user_response import UserResponse
from clever.models.users_created import UsersCreated
from clever.models.users_deleted import UsersDeleted
from clever.models.users_response import UsersResponse
from clever.models.users_updated import UsersUpdated
