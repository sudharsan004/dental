from calendar_api.calendar_api import google_calendar_api
m=google_calendar_api()
m.create_event(calendar_id='dentalsite',
start='2020,12,5,15,00,00',
end='2020,12,5,15,15,00',
desc='food',
)