from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import CourseListView, ModuleDetailView

urlpatterns = [
    path('mine/', views.ManageCourseListView.as_view(), name='manage_course_list'),
    path('create/', views.CourseCreateView.as_view(), name='course_create'),
    path('<pk>/edit/', views.CourseUpdateView.as_view(), name='course_edit'),
    path('<pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
    path('<pk>/module/', views.CourseModuleUpdateView.as_view(), name='course_module_update'),
    path('module/<int:module_id>/content/create/', views.ContentUpload.as_view(),
         name='module_content_create'),
    path('module/<int:module_id>/content/<content_id>/',
         views.ContentUpload.as_view(),
         name='module_content_update'),


    path('', CourseListView.as_view(), name='courses'),
    path('category/<slug:category>/', CourseListView.as_view(),  name='course_list_category'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('module/detail/<int:pk>/',  ModuleDetailView.as_view(), name='module_detail'),

    path('module/<int:module_id>/', views.ModuleContentListView.as_view(), name='module_content_list'),
    path('content/<int:id>/delete/', views.ContentDeleteView.as_view(), name='module_content_delete'),

    path('enroll-course/', views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),

]
