from subfind.release import ReleaseScoring
from subfind_provider.movie_parser import parse_release_name


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'

    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


class ReleaseScoringAlice(ReleaseScoring):
    def sort(self, release_name, releases):
        raw_release_info = parse_release_name(release_name)

        release_tokens = set(raw_release_info['release_tokens'])
        for release in releases:
            release_info = parse_release_name(release['name'])
            release.update(release_info)

            # d =
            # print(release)
            # raise SystemExit

            release['d'] = len(release_tokens.intersection(release['release_tokens'])) * 100 - len(release['release_tokens'])

        def movie_cmp(a, b):
            if a['d'] < b['d']:
                # smaller distances is better
                return -1
            elif a['d'] > b['d']:
                return 1

            if a['year'] > b['year']:
                # larger year is better
                return -1
            elif a['year'] < b['year']:
                return 1

            return 0

        releases.sort(key=cmp_to_key(movie_cmp))
