<?php
/**
 * Copyright since 2007 PrestaShop SA and Contributors
 * PrestaShop is an International Registered Trademark & Property of PrestaShop SA
 *
 * NOTICE OF LICENSE
 *
 * This source file is subject to the Academic Free License version 3.0
 * that is bundled with this package in the file LICENSE.md.
 * It is also available through the world-wide-web at this URL:
 * https://opensource.org/licenses/AFL-3.0
 * If you did not receive a copy of the license and are unable to
 * obtain it through the world-wide-web, please send an email
 * to license@prestashop.com so we can send you a copy immediately.
 *
 * @author    PrestaShop SA and Contributors <contact@prestashop.com>
 * @copyright Since 2007 PrestaShop SA and Contributors
 * @license   https://opensource.org/licenses/AFL-3.0 Academic Free License version 3.0
 */

namespace PrestaShop\Module\PrestashopCheckout\Exception;

class PayPalException extends PsCheckoutException
{
    const ACTION_DOES_NOT_MATCH_INTENT = 1;
    const AGREEMENT_ALREADY_CANCELLED = 2;
    const AMOUNT_CANNOT_BE_SPECIFIED = 3;
    const AMOUNT_MISMATCH = 4;
    const AMOUNT_NOT_PATCHABLE = 5;
    const AUTH_CAPTURE_NOT_ENABLED = 6;
    const AUTHENTICATION_FAILURE = 7;
    const AUTHORIZATION_AMOUNT_EXCEEDED = 8;
    const PAYEE_NOT_CONSENTED = 9;
    const PAYEE_ACCOUNT_NOT_VERIFIED = 10;
    const PAYEE_ACCOUNT_NOT_SUPPORTED = 11;
    const UNSUPPORTED_PAYMENT_INSTRUCTION = 12;
    const UNSUPPORTED_PATCH_PARAMETER_VALUE = 13;
    const UNSUPPORTED_INTENT = 14;
    const TRANSACTION_REFUSED = 15;
    const TRANSACTION_RECEIVING_LIMIT_EXCEEDED = 16;
    const TRANSACTION_LIMIT_EXCEEDED = 17;
    const TRANSACTION_BLOCKED_BY_PAYEE = 18;
    const TRANSACTION_AMOUNT_EXCEEDS_MONTHLY_MAX_LIMIT = 19;
    const TAX_TOTAL_REQUIRED = 20;
    const TAX_TOTAL_MISMATCH = 21;
    const SHIPPING_OPTIONS_NOT_SUPPORTED = 22;
    const SHIPPING_OPTION_NOT_SELECTED = 23;
    const SHIPPING_ADDRESS_INVALID = 24;
    const DUPLICATE_REFERENCE_ID = 25;
    const REFERENCE_ID_REQUIRED = 26;
    const REFERENCE_ID_NOT_FOUND = 27;
    const REDIRECT_PAYER_FOR_ALTERNATE_FUNDING = 28;
    const PREFERRED_SHIPPING_OPTION_AMOUNT_MISMATCH = 29;
    const POSTAL_CODE_REQUIRED = 30;
    const PERMISSION_DENIED = 31;
    const PAYMENT_INSTRUCTION_REQUIRED = 32;
    const PAYEE_NOT_ENABLED_FOR_CARD_PROCESSING = 33;
    const PAYER_COUNTRY_NOT_SUPPORTED = 34;
    const PAYER_CONSENT_REQUIRED = 35;
    const PAYER_CANNOT_PAY = 36;
    const PAYER_ACCOUNT_RESTRICTED = 37;
    const PAYER_ACCOUNT_LOCKED_OR_CLOSED = 38;
    const PAYEE_BLOCKED_TRANSACTION = 39;
    const PAYEE_ACCOUNT_RESTRICTED = 40;
    const PAYEE_ACCOUNT_LOCKED_OR_CLOSED = 41;
    const PAYEE_ACCOUNT_INVALID = 42;
    const PATCH_VALUE_REQUIRED = 43;
    const PATCH_PATH_REQUIRED = 44;
    const PARAMETER_VALUE_NOT_SUPPORTED = 45;
    const ORDER_PREVIOUSLY_VOIDED = 46;
    const ORDER_NOT_SAVED = 47;
    const ORDER_NOT_APPROVED = 48;
    const ORDER_EXPIRED = 49;
    const ORDER_COMPLETED_OR_VOIDED = 50;
    const ORDER_CANNOT_BE_SAVED = 51;
    const ORDER_ALREADY_COMPLETED = 52;
    const ORDER_ALREADY_CAPTURED = 53;
    const ORDER_ALREADY_AUTHORIZED = 54;
    const NOT_SUPPORTED = 55;
    const NOT_PATCHABLE = 56;
    const NOT_ENABLED_FOR_CARD_PROCESSING = 57;
    const NOT_AUTHORIZED = 58;
    const INVALID_PICKUP_ADDRESS = 59;
    const MULTIPLE_SHIPPING_OPTION_SELECTED = 60;
    const MULTIPLE_SHIPPING_ADDRESS_NOT_SUPPORTED = 61;
    const MULTI_CURRENCY_ORDER = 62;
    const MISSING_SHIPPING_ADDRESS = 63;
    const MISSING_REQUIRED_PARAMETER = 64;
    const MAX_VALUE_EXCEEDED = 65;
    const MAX_NUMBER_OF_PAYMENT_ATTEMPTS_EXCEEDED = 66;
    const MAX_AUTHORIZATION_COUNT_EXCEEDED = 67;
    const ITEM_TOTAL_REQUIRED = 68;
    const ITEM_TOTAL_MISMATCH = 69;
    const INVALID_STRING_LENGTH = 70;
    const INVALID_RESOURCE_ID = 71;
    const INVALID_PAYER_ID = 72;
    const INVALID_PATCH_OPERATION = 73;
    const INVALID_PARAMETER = 74;
    const INVALID_PARAMETER_VALUE = 75;
    const INVALID_PARAMETER_SYNTAX = 76;
    const INVALID_JSON_POINTER_FORMAT = 77;
    const INVALID_CURRENCY_CODE = 78;
    const INVALID_COUNTRY_CODE = 79;
    const INVALID_ARRAY_MIN_ITEMS = 80;
    const INVALID_ARRAY_MAX_ITEMS = 81;
    const INVALID_ACCOUNT_STATUS = 82;
    const INTERNAL_SERVICE_ERROR = 83;
    const INTERNAL_SERVER_ERROR = 84;
    const INSTRUMENT_DECLINED = 85;
    const FIELD_NOT_PATCHABLE = 86;
    const DUPLICATE_REQUEST_ID = 87;
    const DUPLICATE_INVOICE_ID = 88;
    const DOMESTIC_TRANSACTION_REQUIRED = 89;
    const DECIMAL_PRECISION = 90;
    const CURRENCY_NOT_SUPPORTED_FOR_COUNTRY = 91;
    const CONSENT_NEEDED = 92;
    const COMPLIANCE_VIOLATION = 93;
    const CITY_REQUIRED = 94;
    const INVALID_SECURITY_CODE_LENGTH = 95;
    const CARD_TYPE_NOT_SUPPORTED = 96;
    const CANNOT_BE_ZERO_OR_NEGATIVE = 97;
    const CANNOT_BE_NEGATIVE = 98;
    const BILLING_AGREEMENT_NOT_FOUND = 99;
    const REFUND_TIME_LIMIT_EXCEEDED = 100;
    const REFUND_NOT_ALLOWED = 101;
    const REFUND_FAILED_INSUFFICIENT_FUNDS = 102;
    const REFUND_CAPTURE_CURRENCY_MISMATCH = 103;
    const REFUND_AMOUNT_EXCEEDED = 104;
    const PREVIOUSLY_VOIDED = 105;
    const PREVIOUSLY_CAPTURED = 106;
    const PERMISSION_NOT_GRANTED = 107;
    const PENDING_CAPTURE = 108;
    const PARTIAL_REFUND_NOT_ALLOWED = 109;
    const MAX_NUMBER_OF_REFUNDS_EXCEEDED = 110;
    const MAX_CAPTURE_COUNT_EXCEEDED = 111;
    const MAX_CAPTURE_AMOUNT_EXCEEDED = 112;
    const INVALID_STRING_MAX_LENGTH = 113;
    const INVALID_PLATFORM_FEES_AMOUNT = 114;
    const INVALID_PAYEE_ACCOUNT = 115;
    const DECIMALS_NOT_SUPPORTED = 116;
    const CAPTURE_FULLY_REFUNDED = 117;
    const CAPTURE_DISPUTED_PARTIAL_REFUND_NOT_ALLOWED = 118;
    const REFUND_NOT_PERMITTED_DUE_TO_CHARGEBACK = 119;
    const CANNOT_BE_VOIDED = 120;
    const AUTHORIZATION_VOIDED = 121;
    const AUTHORIZATION_EXPIRED = 122;
    const AUTHORIZATION_DENIED = 123;
    const AUTHORIZATION_ALREADY_CAPTURED = 124;
    const AUTH_CAPTURE_CURRENCY_MISMATCH = 125;
    const CURRENCY_NOT_SUPPORTED_FOR_CARD_TYPE = 126;
    const NO_EXTERNAL_FUNDING_DETAILS_FOUND = 127;
}
