from sentry.notifications.notification_action.registry import issue_alert_handler_registry
from sentry.notifications.notification_action.types import TicketingIssueAlertHandler
from sentry.workflow_engine.models import Action


@issue_alert_handler_registry.register(Action.Type.GITLAB)
class GitlabIssueAlertHandler(TicketingIssueAlertHandler):
    label_template = "Create a GitLab issue in {integration} with these "
