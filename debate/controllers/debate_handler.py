from django.shortcuts import get_object_or_404

from base.utils.string import get_string_matching_coefficient

from case.models import Case

from debate.exceptions import RebuttalFailedException
from debate.models import Debate

from tracker.controllers.location_handler import LocationHandler


class DebateHandler:

    def __init__(self, case_uuid):
        self.case = Case.objects.get(uuid=case_uuid)

    @staticmethod
    def get_based_on_case(case_uuid: str):
        case = Case.objects.get(uuid=case_uuid)
        debates = Debate.objects.filter(
            case=case,
            pointer__isnull=True
        )
        rebuttal_debates = Debate.objects.get(
            pointer__in=debates
        ).order_by('pointer')
        sorted_debate_list = []
        for debate in debates:
            sorted_debate_list.append(debate)


    @staticmethod
    def get(debate_uuid: str):
        return get_object_or_404(Debate, uuid=debate_uuid)

    def create(self, user, ip_address, **kwargs):
        debate = Debate.objects.create(**{
            'profile': user.profile,
            'case': self.case,
            'comment': kwargs['comment'],
            'inclination': kwargs.get('inclination'),
            'location': LocationHandler().get_location(ip_address)
        })
        return debate

    def create_rebuttal(self, user, **kwargs):
        original_debate = self.get(kwargs['debate_uuid'])
        if original_debate and not original_debate.pointer:
            debate = Debate.objects.create(**{
                'profile': user.profile,
                'case': self.case,
                'comment': kwargs['comment'],
                'inclination': kwargs.get('inclination'),
                'pointer': original_debate
            })
            return debate
        raise RebuttalFailedException('Failed to upload rebuttal to the specific debate.')

    @staticmethod
    def update(debate_uuid, **kwargs):
        debate = Debate.objects.get(uuid=debate_uuid)
        if kwargs.get('comment') and (get_string_matching_coefficient(debate.comment, kwargs.get('comment'))) > 0.8:
            debate.comment = kwargs.get('comment')
        debate.inclination = kwargs.get('inclination', debate.inclination)
        debate.save()
        return debate

    @staticmethod
    def delete(debate_uuid):
        debate = Debate.objects.get(uuid=debate_uuid)
        debate.delete()
