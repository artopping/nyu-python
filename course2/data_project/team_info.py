#!/usr/bin/env python3 


def project_teams(x):
    if x in ['jevans', 'jhoule', 'mpuello', 'kyang']:
        return 'applications'
    elif x in ['rdw', 'ysaxena', 'scarnes']:
        return 'development'
    elif  x in ['smeltzer', 'tpenn', 'awestfall']:
        return 'infrastructure'
    else:
        return 'other'




