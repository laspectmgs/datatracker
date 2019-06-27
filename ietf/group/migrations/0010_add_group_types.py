# Copyright The IETF Trust 2019, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-09 09:02



from django.db import migrations

import debug                            # pyflakes:ignore

group_type_features = {
    'adhoc': {
        'grouptypename': {
            "slug": 'adhoc',
            "desc": 'Ad Hoc schedulable Group Type, for instance HotRfc',
            "name": "Ad Hoc",
            "order": 0,
            "used": True,
            "verbose_name": "Ad Hoc Group Type",
        },
        'groupfeatures': {
            'about_page': 'ietf.group.views.group_about',
            'acts_like_wg': False,
            'admin_roles': '["chair"]',
            'agenda_type_id': 'ietf',
            'create_wiki': True,
            'custom_group_roles': False,
            'customize_workflow': False,
            'default_tab': 'ietf.group.views.group_about',
            'docman_roles': '["chair"]',
            'groupman_roles': '["chair","delegate"]',
            'has_chartering_process': False,
            'has_default_jabber': True,
            'has_documents': False,
            'has_dependencies': False,
            'has_meetings': True,
            'has_milestones': False,
            'has_nonsession_materials': False,
            'has_reviews': False,
            'has_session_materials': True,
            'is_schedulable': True,
            'material_types': '["slides"]',
            'matman_roles': '["chair","delegate"]',
            'req_subm_approval': True,
            'role_order': '["chair","delegate"]',
            'show_on_agenda': True,
        },
    },
    'iesg': {
        'grouptypename': {
            "slug": 'iesg',
            "desc": '',
            "name": "IESG",
            "order": 0,
            "used": True,
            "verbose_name": "Internet Engineering Steering Group"
        },
        'groupfeatures': {
            'about_page': 'ietf.group.views.group_about',
            'acts_like_wg': False,
            'admin_roles': '["chair"]',
            'agenda_type_id': None,
            'create_wiki': False,
            'custom_group_roles': True,
            'customize_workflow': False,
            'default_tab': 'ietf.group.views.group_about',
            'docman_roles': '["chair"]',
            'groupman_roles': '["chair","delegate"]',
            'has_chartering_process': False,
            'has_default_jabber': False,
            'has_documents': False,
            'has_dependencies': False,
            'has_meetings': False,
            'has_milestones': False,
            'has_nonsession_materials': False,
            'has_reviews': False,
            'has_session_materials': False,
            'is_schedulable': False,
            'material_types': '[]',
            'matman_roles': '["chair","delegate"]',
            'req_subm_approval': True,
            'role_order': '["chair","secr"]',
            'show_on_agenda': False
        },
    },
    'ise': {
        'grouptypename': {
            "slug": 'ise',
            "desc": '',
            "name": "ISE",
            "order": 0,
            "used": True,
            "verbose_name": "Independent Stream Editor",
        },
        'groupfeatures': {
            'about_page': 'ietf.group.views.group_about',
            'acts_like_wg': False,
            'admin_roles': '["chair","lead"]',
            'agenda_type_id': None,
            'create_wiki': False,
            'custom_group_roles': True,
            'customize_workflow': False,
            'default_tab': 'ietf.group.views.group_about',
            'docman_roles': '["chair"]',
            'groupman_roles': '["chair","delegate"]',
            'has_chartering_process': False,
            'has_default_jabber': False,
            'has_documents': False,
            'has_dependencies': False,
            'has_meetings': False,
            'has_milestones': False,
            'has_nonsession_materials': False,
            'has_reviews': False,
            'has_session_materials': False,
            'is_schedulable': False,
            'material_types': '[]',
            'matman_roles': '["chair","delegate"]',
            'req_subm_approval': True,
            'role_order': '["chair"]',
            'show_on_agenda': False
        },
    },
}

def forward(apps, schema_editor):
    GroupTypeName = apps.get_model('name', 'GroupTypeName')
    GroupFeatures = apps.get_model('group', 'GroupFeatures')
    for slug in group_type_features:
        typename = group_type_features[slug]['grouptypename']
        gt, _ = GroupTypeName.objects.get_or_create(slug=slug)
        for k,v in list(typename.items()):
            setattr(gt, k, v)
        gt.save()
        #
        features = group_type_features[slug]['groupfeatures']
        gf, _ = GroupFeatures.objects.get_or_create(type_id=slug)
        for k,v in list(features.items()):
            setattr(gf, k, v)
        gf.save()


# This migration does not remove or change any previous fields, and executes
# swirftly, so we permit it to be interleaved with schema migrations
forward.interleavable = True

def reverse(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('group', '0009_auto_20190122_1012'),
    ]

    operations = [
        migrations.RunPython(forward, reverse),
    ]
