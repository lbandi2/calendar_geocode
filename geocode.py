import geocoder
import emoji
from events import get_events, update_event

class Calendar:
    def __init__(self, cal_id, api_key):
        self.cal_id = cal_id
        self.api_key = api_key
        self.events = get_events(self.cal_id)
        self.check_all_events()

    def fetch_events(self):
        events = get_events(self.cal_id)
        return events

    def has_description(self, event):
        if 'description' in event:
            return True
        return False

    def has_country(self, event):
        if self.has_description(event):
            if 'country: ' in event['description']:
                return True
        return False

    def cleanup_title(self, event):
        place = event['summary']
        if '(' in place.split(' ')[-1]:
            place = " ".join(place.split(' ')[:-1]).replace("Viaje a ", "").replace("viaje a ", "")
        else:
            place = place.replace("Viaje a ", "").replace("viaje a ", "")
        return place

    def search_country(self, event):
        place = self.cleanup_title(event)
        print(f"Checking results for {place}..")
        result = geocoder.google(place, key=self.api_key)
        print(f"Found country: {result.country_long}.")
        return result

    def check_all_events(self):
        for event in self.events:
            title = event['summary']
            if not self.has_country(event):
                self.update_event(event)
            else:
                print(f'Skipping {title.encode("utf-8")}')

    def update_event(self, event):
        country = self.search_country(event)
        title = event['summary']
        if not self.has_description(event):
            event['description'] = f"country: {country.country_long.title()}"
        else:
            event['description'] = f"{event['description']}\n\ncountry: {country.country_long.title()}"
        country_flag = emoji.emojize(f":{country.country_long}:")
        print(f"Adding country to {title}")
        event['summary'] = f"{country_flag} {title}"
        update_event(self.cal_id, event['id'], event)
