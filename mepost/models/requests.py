from typing import List, Dict


class AddDomainRequest:
    def __init__(self, domain: str):
        self.domain = domain


class CancelScheduledMessageRequest:
    def __init__(self, scheduled_message_id: str):
        self.scheduled_message_id = scheduled_message_id


class CancelWarmUpRequest:
    def __init__(self, ip_address: str):
        self.ip_address = ip_address


class CreateIpGroupRequest:
    def __init__(self, group_name: str):
        self.group_name = group_name


class CreateNewGroupRequest:
    def __init__(self, name: str, to: List['To']):
        self.name = name
        self.to = to


class CreateSubscriberRequest:
    def __init__(self, to: List['To']):
        self.to = to


class DeleteSubscriberRequest:
    def __init__(self, emails: List[str]):
        self.emails = emails


class RenameGroupRequest:
    def __init__(self, name: str):
        self.name = name


class SendMarketingRequest:
    def __init__(self, from_email: str, from_name: str, subject: str, to: List[str], 
                 html: str = None, text: str = None, headers: Dict[str, str] = None, 
                 attachments: List['AttachmentDto'] = None, customization: Dict[str, str] = None, 
                 ip_group: str = None, return_path: str = None, scheduled_at: str = None):
        self.from_email = from_email
        self.from_name = from_name
        self.subject = subject
        self.to = to
        self.html = html
        self.text = text
        self.headers = headers
        self.attachments = attachments
        self.customization = customization
        self.ip_group = ip_group
        self.return_path = return_path
        self.scheduled_at = scheduled_at


class SendMessageByTemplateRequest:
    def __init__(self, message: 'MessageDto', template_id: str):
        self.message = message
        self.template_id = template_id


class SendTransactionalRequest(SendMarketingRequest):
    pass


class SetIpGroupRequest:
    def __init__(self, group_name: str, ip_address: str):
        self.group_name = group_name
        self.ip_address = ip_address


class StartWarmUpRequest:
    def __init__(self, ip_address: str):
        self.ip_address = ip_address


class To:
    def __init__(self, email: str, name: str, type_: str = None, customization: Dict[str, str] = None):
        self.email = email
        self.name = name
        self.type = type_
        self.customization = customization


class AttachmentDto:
    def __init__(self, base64_content: str, file_name: str):
        self.base64_content = base64_content
        self.file_name = file_name


class MessageDto:
    def __init__(self, from_email: str, from_name: str, subject: str, to: List['To'], 
                 html: str = None, text: str = None, headers: Dict[str, str] = None, 
                 attachments: List['AttachmentDto'] = None, customization: Dict[str, str] = None, 
                 ip_group: str = None, return_path: str = None, scheduled_at: str = None):
        self.from_email = from_email
        self.from_name = from_name
        self.subject = subject
        self.to = to
        self.html = html
        self.text = text
        self.headers = headers
        self.attachments = attachments
        self.customization = customization
        self.ip_group = ip_group
        self.return_path = return_path
        self.scheduled_at = scheduled_at
