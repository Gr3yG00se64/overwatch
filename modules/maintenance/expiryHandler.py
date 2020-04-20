#Local Dependencies
import config

#Package Dependencies
from datetime import datetime, timedelta

def expiredAlertsFinder(alerts):
    expired_alerts = []
    alertExpire = int(config.alertExpiry)

    if alertExpire > 0:

        for alert in alerts:
            alert_datetime = datetime.strptime(alert.get('date'), '%m/%d/%Y')

            days_old = (datetime.now() - alert_datetime).days

            if days_old >= alertExpire:
                expired_alerts.append(alert)

    return expired_alerts