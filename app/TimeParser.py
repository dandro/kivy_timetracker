from datetime import datetime


class TimeParser(object):
    def __init__(self, db_dict):
        self.db_dict = db_dict

    def parse_rows(self):
        report_data = {}
        data = self.get_all_rows(self.db_dict)
        for i in range(0, len(data)):
            current_row = data[i]
            self.add_to_report(current_row, data, i, report_data)

        print"report: {}".format(str(report_data))

    def add_to_report(self, current_row, data, i, report_data):
        if current_row['project_title'].lower() != 'eob':
            current_row['duration'] = self.get_row_duration(data, i)
            if current_row['duration'] is not None and current_row['project_title'] in report_data:
                self.group_logs(report_data, current_row)
            elif current_row['duration'] is not None:
                self.add_new_log(report_data, current_row)

    @staticmethod
    def get_row_duration(data, i):
        current_time = datetime.strptime(data[i]['time'], '%Y-%m-%d %H:%M:%S')
        next_time = datetime.strptime(data[i + 1]['time'], '%Y-%m-%d %H:%M:%S') if i + 1 < len(data) else datetime.now()
        duration = TimeParser.get_duration_str(next_time - current_time)
        return duration if len(duration) > 0 else None

    @staticmethod
    def get_duration_str(duration):
        duration_str = str(duration)
        duration_tuple = datetime.strptime(duration_str[:duration_str.find('.')], '%H:%M:%S').timetuple()
        return TimeParser.format_duration(duration_tuple)

    @staticmethod
    def format_duration(duration_tuple):
        formatted_duration = ''
        if duration_tuple.tm_hour > 0:
            formatted_duration += str(duration_tuple.tm_hour) + 'h'
        if duration_tuple.tm_min > 0:
            separator = ', ' if duration_tuple.tm_hour > 0 else ''
            formatted_duration += separator + str(duration_tuple.tm_min) + 'm'
        return formatted_duration

    @staticmethod
    def get_all_rows(db):
        report_data = []
        row_set = set(db.getall())
        row_list = list(row_set)
        row_list.sort()
        for key in row_list:
            report_data.append(db.get(key))
        return report_data

    @staticmethod
    def group_logs(report_data, current_row):
        report_data[current_row['project_title']]['duration'] += ', ' + current_row['duration']
        if not current_row['project_description'].lower() == report_data[current_row['project_title']][
            'project_description'].lower():
            report_data[current_row['project_title']]['project_description'] += ', ' + current_row[
                'project_description']

    @staticmethod
    def add_new_log(report_data, current_row):
        report_data[current_row['project_title']] = {
            'duration': current_row['duration'],
            'project_description': current_row['project_description']
        }
