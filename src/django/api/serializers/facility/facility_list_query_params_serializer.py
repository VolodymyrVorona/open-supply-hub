from rest_framework.serializers import (
    IntegerField,
    ChoiceField,
    Serializer,
)
from ...constants import MatchResponsibility
from ...models import FacilityList


class FacilityListQueryParamsSerializer(Serializer):
    contributor = IntegerField(required=False)
    match_responsibility = ChoiceField(choices=MatchResponsibility.CHOICES,
                                       required=False)
    status = ChoiceField(choices=[FacilityList.MATCHED, FacilityList.APPROVED,
                                  FacilityList.REJECTED, FacilityList.PENDING,
                                  FacilityList.REPLACED],
                         required=False)
