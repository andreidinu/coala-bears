from coalib.bearlib.abstractions.Linter import linter
from dependency_management.requirements.DistributionRequirement import DistributionRequirement


@linter(executable='tidy',
        output_format='regex',
        output_regex=r'(^line \d+ column \d+ \- (Warning|Error): .*$)')
class HTMLTidyBear:
    """
    Raise HTML code errors and warnings and corrects them.
    Also detects unmatched tags pairs.

    For more information, check this:
    <https://github.com/htacg/tidy-html5>
    """

    LANGUAGES = {'HTML'}
    REQUIREMENTS = {DistributionRequirement(apt_get='tidy')}
    AUTHORS = {'The coala developers'}
    AUTHORS_EMAILS = {'coala-devel@googlegroups.com'}
    LICENSE = 'AGPL-3.0'
    CAN_DETECT = {'Formatting', 'Syntax'}

    @staticmethod
    def create_arguments(filename, file, config_list):
        return '-errors', filename
