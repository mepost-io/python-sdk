from typing import List, Optional


class Response:
    def __init__(self, success: bool, data=None, errors=None):
        self.success = success
        self.data = data
        self.errors = errors


class ErrorResponse:
    def __init__(self, code: int, message: str, type_: str):
        self.code = code
        self.message = message
        self.type = type_


class AddDomainResponse:
    def __init__(self, dkim: 'DNSRecord', dmarc: 'DNSRecord', domain: str, spf: 'DNSRecord'):
        self.dkim = dkim
        self.dmarc = dmarc
        self.domain = domain
        self.spf = spf


class CancelWarmUpResponse:
    def __init__(self, cancelled_at: str, ip_address: str, started_at: str):
        self.cancelled_at = cancelled_at
        self.ip_address = ip_address
        self.started_at = started_at


class GetMessageInfoResponse:
    def __init__(self, email: str, email_clicks_count: int, email_clicks_detail: List['EmailClickDetail'],
                 email_reads_count: int, email_reads_detail: List['EmailReadDetail'], state: str,
                 subject: str, template_id: str):
        self.email = email
        self.email_clicks_count = email_clicks_count
        self.email_clicks_detail = email_clicks_detail
        self.email_reads_count = email_reads_count
        self.email_reads_detail = email_reads_detail
        self.state = state
        self.subject = subject
        self.template_id = template_id


class GetScheduleInfoResponse:
    def __init__(self, details: 'ScheduleDetails', email_reads_count: int, email_reads_unique: int,
                 hard_bounce_count: int, link_clicks_count: int, other_bounce_count: int,
                 sender_from_email: str, sender_from_name: str, soft_bounce_count: int,
                 state: str, subject: str, template_id: str, unsubscribe_count: int):
        self.details = details
        self.email_reads_count = email_reads_count
        self.email_reads_unique = email_reads_unique
        self.hard_bounce_count = hard_bounce_count
        self.link_clicks_count = link_clicks_count
        self.other_bounce_count = other_bounce_count
        self.sender_from_email = sender_from_email
        self.sender_from_name = sender_from_name
        self.soft_bounce_count = soft_bounce_count
        self.state = state
        self.subject = subject
        self.template_id = template_id
        self.unsubscribe_count = unsubscribe_count


class RemoveDomainResponse:
    def __init__(self, domain: str, removed_at: str):
        self.domain = domain
        self.removed_at = removed_at


class SetIpGroupResponse:
    def __init__(self, ip_address: str, ip_group: 'IPGroup'):
        self.ip_address = ip_address
        self.ip_group = ip_group


class StartWarmUpResponse:
    def __init__(self, end_at: str, ip_address: str, start_at: str, status: str):
        self.end_at = end_at
        self.ip_address = ip_address
        self.start_at = start_at
        self.status = status


class DNSRecord:
    def __init__(self, content: str, name: str, type_: str):
        self.content = content
        self.name = name
        self.type = type_


class EmailClickDetail:
    def __init__(self, city: str, country_code: str, ip: str, url: str):
        self.city = city
        self.country_code = country_code
        self.ip = ip
        self.url = url


class EmailReadDetail:
    def __init__(self, city: str, country_code: str, ip: str):
        self.city = city
        self.country_code = country_code
        self.ip = ip


class ScheduleDetails:
    def __init__(self, clicks: List['EmailTransactionEvent'], hard_bounces: List['EmailTransactionEvent'],
                 reads: List['EmailTransactionEvent'], soft_bounces: List['EmailTransactionEvent'],
                 unsubscribes: List['EmailTransactionEvent']):
        self.clicks = clicks
        self.hard_bounces = hard_bounces
        self.reads = reads
        self.soft_bounces = soft_bounces
        self.unsubscribes = unsubscribes


class EmailTransactionEvent:
    def __init__(self, bounce_code: Optional[str], city: Optional[str], country_code: Optional[str],
                 created_at: Optional[str], data: Optional[str], event_type: Optional[str], id_: Optional[str],
                 ip: Optional[str], stat_id: Optional[str], subscriber_id: Optional[str],
                 transaction_id: Optional[str]):
        self.bounce_code = bounce_code
        self.city = city
        self.country_code = country_code
        self.created_at = created_at
        self.data = data
        self.event_type = event_type
        self.id = id_
        self.ip = ip
        self.stat_id = stat_id
        self.subscriber_id = subscriber_id
        self.transaction_id = transaction_id


class IPGroup:
    def __init__(self, company_id: int, created_at: str, ip_addresses: List['IpAddress'],
                 name: str, updated_at: str, uuid: str):
        self.company_id = company_id
        self.created_at = created_at
        self.ip_addresses = ip_addresses
        self.name = name
        self.updated_at = updated_at
        self.uuid = uuid


class IpAddress:
    def __init__(self, company_id: int, created_at: str, ip: str, ip_group_id: int,
                 reverse_dns: Optional[str], status: str, updated_at: str, uuid: str):
        self.company_id = company_id
        self.created_at = created_at
        self.ip = ip
        self.ip_group_id = ip_group_id
        self.reverse_dns = reverse_dns
        self.status = status
        self.updated_at = updated_at
        self.uuid = uuid


class Subscriber:
    def __init__(self, bounced: bool, confirm_code: str, confirm_ip: str, confirmed: bool,
                 created_at: str, custom_fields: List['CustomField'], email_address: str,
                 email_group_id: int, subscribed_at: str, unsubscribed: bool, updated_at: str, uuid: str):
        self.bounced = bounced
        self.confirm_code = confirm_code
        self.confirm_ip = confirm_ip
        self.confirmed = confirmed
        self.created_at = created_at
        self.custom_fields = custom_fields
        self.email_address = email_address
        self.email_group_id = email_group_id
        self.subscribed_at = subscribed_at
        self.unsubscribed = unsubscribed
        self.updated_at = updated_at
        self.uuid = uuid


class CustomField:
    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value


class BaseResult:
    def __init__(self, data: List, total: int):
        self.data = data
        self.total = total


class Schedule:
    def __init__(self, approved: bool, authorized_to_send: bool, created_at: str, credit_amount: float,
                 email_group_id: int, job_status: str, job_type: str, reason: str, result_type: str,
                 scheduled_at: str, stat_id: str, template: 'Template', updated_at: str, uuid: str):
        self.approved = approved
        self.authorized_to_send = authorized_to_send
        self.created_at = created_at
        self.credit_amount = credit_amount
        self.email_group_id = email_group_id
        self.job_status = job_status
        self.job_type = job_type
        self.reason = reason
        self.result_type = result_type
        self.scheduled_at = scheduled_at
        self.stat_id = stat_id
        self.template = template
        self.updated_at = updated_at
        self.uuid = uuid


class Template:
    def __init__(self, config: str, created_at: str, name: str, raw_html: str, raw_text: str,
                 subject: str, updated_at: str, uuid: str):
        self.config = config
        self.created_at = created_at
        self.name = name
        self.raw_html = raw_html
        self.raw_text = raw_text
        self.subject = subject
        self.updated_at = updated_at
        self.uuid = uuid


class EmailGroupWithCounts:
    def __init__(self, company_id: int, created_at: str, general_score: int, is_web: bool, name: str,
                 newsletter_score: int, priority: int, total_active_subscriber: int, total_bounced: int,
                 total_subscriber: int, total_unsubscribe: int, updated_at: str, uuid: str):
        self.company_id = company_id
        self.created_at = created_at
        self.general_score = general_score
        self.is_web = is_web
        self.name = name
        self.newsletter_score = newsletter_score
        self.priority = priority
        self.total_active_subscriber = total_active_subscriber
        self.total_bounced = total_bounced
        self.total_subscriber = total_subscriber
        self.total_unsubscribe = total_unsubscribe
        self.updated_at = updated_at
        self.uuid = uuid


class EmailGroup:
    def __init__(self, company_id: int, created_at: str, general_score: int, is_web: bool, name: str,
                 newsletter_score: int, priority: int, total_active_subscriber: int, total_subscriber: int,
                 total_unsubscribe: int, updated_at: str, uuid: str):
        self.company_id = company_id
        self.created_at = created_at
        self.general_score = general_score
        self.is_web = is_web
        self.name = name
        self.newsletter_score = newsletter_score
        self.priority = priority
        self.total_active_subscriber = total_active_subscriber
        self.total_subscriber = total_subscriber
        self.total_unsubscribe = total_unsubscribe
        self.updated_at = updated_at
        self.uuid = uuid


class CompanyDomain:
    def __init__(self, aws_region: str, aws_verified: bool, company: 'Company', company_id: int,
                 created_at: str, dkim_content: str, dkim_name: str, dkim_private_key: str,
                 dkim_selector: str, dkim_verified: bool, dmarc_content: str, dmarc_name: str,
                 dmarc_verified: bool, domain: str, has_aws_identity: bool, is_verified: bool,
                 spf_content: str, spf_name: str, spf_verified: bool, updated_at: str, uuid: str):
        self.aws_region = aws_region
        self.aws_verified = aws_verified
        self.company = company
        self.company_id = company_id
        self.created_at = created_at
        self.dkim_content = dkim_content
        self.dkim_name = dkim_name
        self.dkim_private_key = dkim_private_key
        self.dkim_selector = dkim_selector
        self.dkim_verified = dkim_verified
        self.dmarc_content = dmarc_content
        self.dmarc_name = dmarc_name
        self.dmarc_verified = dmarc_verified
        self.domain = domain
        self.has_aws_identity = has_aws_identity
        self.is_verified = is_verified
        self.spf_content = spf_content
        self.spf_name = spf_name
        self.spf_verified = spf_verified
        self.updated_at = updated_at
        self.uuid = uuid


class Company:
    def __init__(self, company_plan: 'CompanyPlan', company_plan_id: int, created_at: str, footer_html: str,
                 footer_text: str, name: str, owner_id: int, priority: int, updated_at: str, uuid: str):
        self.company_plan = company_plan
        self.company_plan_id = company_plan_id
        self.created_at = created_at
        self.footer_html = footer_html
        self.footer_text = footer_text
        self.name = name
        self.owner_id = owner_id
        self.priority = priority
        self.updated_at = updated_at
        self.uuid = uuid


class CompanyPlan:
    def __init__(self, company_id: int, created_at: str, current_usage: int, ended_at: str,
                 last_billed: str, pricing_plan: 'PricingPlan', pricing_plan_id: int,
                 selected_contacts_limit: int, selected_data_retention: int, selected_email_limit: int,
                 started_at: str, status: str, updated_at: str, uuid: str):
        self.company_id = company_id
        self.created_at = created_at
        self.current_usage = current_usage
        self.ended_at = ended_at
        self.last_billed = last_billed
        self.pricing_plan = pricing_plan
        self.pricing_plan_id = pricing_plan_id
        self.selected_contacts_limit = selected_contacts_limit
        self.selected_data_retention = selected_data_retention
        self.selected_email_limit = selected_email_limit
        self.started_at = started_at
        self.status = status
        self.updated_at = updated_at
        self.uuid = uuid


class PricingPlan:
    def __init__(self, created_at: str, daily_limit: int, maximum_email: int, name: str,
                 plan_type: str, updated_at: str, uuid: str):
        self.created_at = created_at
        self.daily_limit = daily_limit
        self.maximum_email = maximum_email
        self.name = name
        self.plan_type = plan_type
        self.updated_at = updated_at
        self.uuid = uuid
