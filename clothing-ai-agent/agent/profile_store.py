from models.profile import UserProfile

_profile = UserProfile()


def get_profile() -> UserProfile:
    return _profile


def update_profile(**kwargs) -> UserProfile:
    global _profile
    data = _profile.model_dump()
    data.update(kwargs)
    _profile = UserProfile(**data)
    return _profile