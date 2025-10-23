from pywinauto import Application, keyboard, mouse
from locators.locators import LocOrders
from locators.function import Function
import time
import subprocess
import psutil


class WinAISTApp:
    def __init__(self):
        self.fun = Function()
        self.loc = LocOrders()
        self.app = self.fun.app

    def finance(self):
        # 1. Запуск приложения
        self.fun.start_application()
        time.sleep(3)

        # 3.
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(1)

        self.fun.click_element_sp(main_window, self.loc.FINANCE)
        time.sleep(3)
        self.fun.click_element_sp(main_window, self.loc.OUTGOING_INVOICES)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.ADD_BUTTON)
        time.sleep(1)
        main_window = self.fun.get_check_form()
        main_window.set_focus()

        self.fun.order_data = {
            'is_number': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_NUMBER,"Value"),
            'is_list': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_LIST,"Value"),
            'is_date': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_DATE,"Value"),
            'is_note': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE_SERVICES,"Value"),
            'is_date_sf': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_DATE_SF, "Value"),

            'is_supplier': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_SUPPLIER, "Value"),
            'is_buyer': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_BUYER, "Value"),
            'is_client': self.fun.get_element_property_sp(main_window, self.fun.loc.GTD_CLIENT, "Value"),
            'is_number_order': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_NUMBER_ORDER, "Value"), #добавить в проверку

            'is_ocean_vessel': self.fun.get_element_property_sp(main_window, self.fun.loc.OCEAN_VESSEL_PANEL, "Value"),
            'is_feeder_vessel': self.fun.get_element_property_sp(main_window, self.fun.loc.FEEDER_VESSEL_PANEL, "Value"),
            'is_ocean_ship': self.fun.get_element_property_sp(main_window, self.fun.loc.OCEAN_SHIP_PANEL, "Value"),
            'is_feeder_ship': self.fun.get_element_property_sp(main_window, self.fun.loc.FEEDER_SHIP_PANEL, "Value"),
            'is_arrival': self.fun.get_element_property_sp(main_window, self.fun.loc.ARRIVAL_PANEL, "Value"),
            'is_shipment': self.fun.get_element_property_sp(main_window, self.fun.loc.SHIPMENT_PANEL, "Value"),
            'is_loading_conditions': self.fun.get_element_property_sp(main_window, self.fun.loc.LOADING_CONDITIONS_PANEL, "Value"),
            'is_destination_conditions': self.fun.get_element_property_sp(main_window, self.fun.loc.DESTINATION_CONDITIONS_PANEL, "Value"),
            'is_terminal': self.fun.get_element_property_sp(main_window, self.fun.loc.TERMINAL_PANEL, "Value"),
            'is_ocean_line': self.fun.get_element_property_sp(main_window, self.fun.loc.OCEAN_LINE_PANEL, "Value"),
            'is_feeder_line': self.fun.get_element_property_sp(main_window, self.fun.loc.FEEDER_LINE_PANEL, "Value"),
            'is_loading_location': self.fun.get_element_property_sp(main_window, self.fun.loc.LOADING_LOCATION_PANEL, "Value"),
            'is_destination': self.fun.get_element_property_sp(main_window, self.fun.loc.DESTINATION_PANEL, "Value"),

            'is_return_date': self.fun.get_element_property_sp(main_window, self.fun.loc.RETURN_DATE_PANEL, "Value"),
            'is_pickup_date': self.fun.get_element_property_sp(main_window, self.fun.loc.PICKUP_DATE_PANEL, "Value"),
            'is_gtd': self.fun.get_element_property_sp(main_window, self.fun.loc.GTD_PANEL, "Value"),
        }
        self.fun.click_element(main_window, self.loc.EXPAND, timeout=1)

        # Редактирование формы
        self.fun.click_element_sp(main_window, self.loc.IS_LIST)
        self.fun.click_element_sp(main_window, self.loc.IS_FREIGHT)
        self.fun.set_text_field(main_window, self.fun.loc.NOTE_SERVICES, "Примечание для ИС", timeout=1)
        self.fun.click_element(main_window, self.fun.loc.IS_DATE_SF, timeout=1)
        keyboard.send_keys('1')
        self.fun.click_element_sp(main_window, self.loc.IS_SUPPLIER)
        self.fun.set_text_field(main_window, self.fun.loc.SEARCH_BOX, "бодрус", timeout=1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_4)
        self.fun.click_element_sp(main_window, self.loc.GTD_CLIENT)
        self.fun.set_text_field(main_window, self.fun.loc.SEARCH_BOX, "Веспа", timeout=1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.IS_ORDER)
        self.fun.click_element_sp(main_window, self.loc.FREIGHT_ORDER_CREATE)
        self.fun.click_element_sp(main_window, self.loc.ORDER_TYPE_COMBO)
        self.fun.click_element_sp(main_window, self.loc.LOGISTICS_ITEM)
        self.fun.click_element_sp(main_window, self.loc.CUSTOMER_COMBO)
        self.fun.set_text_field(main_window, self.fun.loc.SEARCH_BOX, "Веспа", timeout=1)
        self.fun.click_element(main_window, self.loc.RECIPIENT_1, timeout=1)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)
        time.sleep(1)

        self.fun.click_element_sp(main_window, self.loc.LOADING_CONDITIONS_PANEL)
        self.fun.click_element_sp(main_window, self.loc.DOOR)
        self.fun.click_element_sp(main_window, self.loc.DESTINATION_CONDITIONS_PANEL)
        self.fun.click_element_sp(main_window, self.loc.FOB)

        self.fun.click_element_sp(main_window, self.loc.LOADING_LOCATION_PANEL)
        self.fun.set_text_field(main_window, self.fun.loc.SEARCH_BOX, "F", timeout=1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.TERMINAL_PANEL)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)

        self.fun.click_element_sp(main_window, self.loc.DESTINATION_PANEL)
        self.fun.set_text_field(main_window, self.fun.loc.SEARCH_BOX, "D", timeout=1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.SHIPMENT_PANEL)
        keyboard.send_keys('2')
        self.fun.click_element_sp(main_window, self.loc.ARRIVAL_PANEL)
        keyboard.send_keys('3')

        self.fun.click_element_sp(main_window, self.loc.OCEAN_LINE_PANEL)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.FEEDER_LINE_PANEL)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_2)
        self.fun.click_element_sp(main_window, self.loc.OCEAN_VESSEL_PANEL)
        keyboard.send_keys('4')
        self.fun.click_element_sp(main_window, self.loc.FEEDER_VESSEL_PANEL)
        keyboard.send_keys('5')
        self.fun.click_element_sp(main_window, self.loc.OCEAN_SHIP_PANEL)
        self.fun.set_text_field(main_window, self.fun.loc.OCEAN_SHIP_PANEL, "Судно для океана", timeout=1)
        self.fun.click_element_sp(main_window, self.loc.FEEDER_SHIP_PANEL)
        self.fun.set_text_field(main_window, self.fun.loc.FEEDER_SHIP_PANEL, "Судно для рек", timeout=1)

        self.fun.set_text_field(main_window, self.fun.loc.GTD_PANEL, "123", timeout=1)
        self.fun.click_element_sp(main_window, self.loc.PICKUP_DATE_PANEL)
        keyboard.send_keys('6')
        self.fun.click_element_sp(main_window, self.loc.RETURN_DATE_PANEL)
        keyboard.send_keys('7')

        self.fun.click_element_sp(main_window, self.loc.APPLY_BUTTON)
        time.sleep(2)
        self.fun.order_data.update({
            'is_number_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_NUMBER, "Value"),
            'is_list_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_LIST, "Value"),
            'is_date_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_DATE, "Value"),
            'is_note_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE_SERVICES, "Value"),
            'is_sync': self.fun.get_element_property_sp(main_window, self.fun.loc.SYNC_1C, "Value"),
            'is_date_sf_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_DATE_SF, "Value"),

            'is_supplier_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_SUPPLIER, "Value"),
            'is_buyer_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_BUYER, "Value"),
            'is_client_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.GTD_CLIENT, "Value"),
            'is_number_order_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_NUMBER_ORDER, "Value"),

            'is_ocean_vessel_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.OCEAN_VESSEL_PANEL, "Value"),
            'is_feeder_vessel_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.FEEDER_VESSEL_PANEL,"Value"),
            'is_ocean_ship_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.OCEAN_SHIP_PANEL, "Value"),
            'is_feeder_ship_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.FEEDER_SHIP_PANEL, "Value"),
            'is_arrival_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.ARRIVAL_PANEL, "Value"),
            'is_shipment_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.SHIPMENT_PANEL, "Value"),
            'is_loading_conditions_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.LOADING_CONDITIONS_PANEL, "Value"),
            'is_destination_conditions_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.DESTINATION_CONDITIONS_PANEL,"Value"),
            'is_terminal_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.TERMINAL_PANEL, "Value"),
            'is_ocean_line_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.OCEAN_LINE_PANEL, "Value"),
            'is_feeder_line_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.FEEDER_LINE_PANEL, "Value"),
            'is_loading_location_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.LOADING_LOCATION_PANEL,
                                                                    "Value"),

            'is_destination_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.DESTINATION_PANEL, "Value"),
            'is_return_date_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.RETURN_DATE_PANEL, "Value"),
            'is_pickup_date_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.PICKUP_DATE_PANEL, "Value"),
            'is_gtd_mod': self.fun.get_element_property_sp(main_window, self.fun.loc.GTD_PANEL, "Value"),
        })
        text = self.fun.get_element_value(main_window, self.loc.IS_NUMBER, timeout=1)

        # Добавить услугу
        self.fun.click_element_sp(main_window, self.loc.TAB_SERVICES)
        self.fun.click_element_sp(main_window, self.loc.ADD_BUTTON)
        time.sleep(1)
        main_window = self.fun.get_services_form()
        main_window.set_focus()
        self.fun.click_element_sp(main_window, self.loc.SERVICES_SERVICES)
        self.fun.set_text_field(main_window, self.fun.loc.SEARCH_BOX, "Автоперевозка собственным транспортом", timeout=1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.set_text_field(main_window, self.loc.SERVICES_BET, "100", timeout=1)
        self.fun.click_element_sp(main_window, self.loc.SERVICES_CURRENCY)
        self.fun.click_element_sp(main_window, self.loc.RUR)
        self.fun.click_element_sp(main_window, self.loc.NDS)
        self.fun.click_element_sp(main_window, self.loc.NDS_0)
        self.fun.click_element_sp(main_window, self.loc.APPLY_BUTTON)
        self.fun.order_data.update({
            'service_service': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICES_SERVICES, "Value"),
            'service_dns': self.fun.get_element_property_sp(main_window, self.fun.loc.NDS, "Value"),
            'service_rate': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICES_BET, "Value"),
            'quantity_service': self.fun.get_element_property_sp(main_window, self.fun.loc.QUANTITY_SERVICE,"Value"),
            'service_vat': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICES_CURRENCY, "Value"),
        })


        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)
        time.sleep(1)

        main_window = self.fun.get_check_form()
        main_window.set_focus()

        self.fun.order_data.update({
            'service_line_number1': self.fun.get_element_property_sp(main_window, self.fun.loc.LINE_NUMBER1, "Value"),
            'service_service1': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_LINE1, "Value"),
            'service_vat1': self.fun.get_element_property_sp(main_window, self.fun.loc.VAT_LINE1, "Value"),
            'service_quantity1': self.fun.get_element_property_sp(main_window, self.fun.loc.QUANTITY_LINE1, "Value"),
            'service_rate1': self.fun.get_element_property_sp(main_window, self.fun.loc.RATE_LINE1, "Value"),
            'service_currency1': self.fun.get_element_property_sp(main_window, self.fun.loc.CURRENCY_LINE1, "Value"),
            'service_total1': self.fun.get_element_property_sp(main_window, self.fun.loc.TOTAL_LINE1, "Value"),
            'service_total_sv1': self.fun.get_element_property_sp(main_window, self.fun.loc.TOTAL_SV_LINE1, "Value"),

            'service_total': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_TOTAL, "Value"),

        })

        # Связываем с Вх. платежом
        self.fun.click_element_sp(main_window, self.loc.INCOMING_PAYMENTS1)
        self.fun.click_element_sp(main_window, self.loc.CONNECT_VP)
        time.sleep(2)
        self.fun.click_element_sp(main_window, self.loc.SERVICES_OPTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.ADD_SERVICES)
        time.sleep(1)
        self.fun.order_data.update({
            'service_date': self.fun.get_element_property_sp(main_window, self.fun.loc.DATE_LINE1, "Value"),
            'service_invoice': self.fun.get_element_property_sp(main_window, self.fun.loc.INVOICE_LINE1, "Value"),
            'service_client': self.fun.get_element_property_sp(main_window, self.fun.loc.CLIENT_LINE1, "Value"),
            'service_buyer': self.fun.get_element_property_sp(main_window, self.fun.loc.BUYER_LINE1, "Value"),
            'service_supplier': self.fun.get_element_property_sp(main_window, self.fun.loc.SUPPLIER_LINE1, "Value"),
            'service_currency': self.fun.get_element_property_sp(main_window, self.fun.loc.CURRENCY_LINE1, "Value"),
            'service_amount': self.fun.get_element_property_sp(main_window, self.fun.loc.AMOUNT_LINE1, "Value"),
            'service_info': self.fun.get_element_property_sp(main_window, self.fun.loc.INFO_LINE1, "Value"),
            'service_closed': self.fun.get_element_property_sp(main_window, self.fun.loc.CLOSED_LINE1, "Value"),
            'service_unpaid': self.fun.get_element_property_sp(main_window, self.fun.loc.UNPAID_LINE1, "Value"),
            'service_charged': self.fun.get_element_property_sp(main_window, self.fun.loc.CHARGED_LINE1, "Value"),
            'service_charged_sv': self.fun.get_element_property_sp(main_window, self.fun.loc.CHARGED_SV_LINE1, "Value"),

        })

        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)
        self.fun.order_data.update({
            'service_date_form': self.fun.get_element_property_sp(main_window, self.fun.loc.DATE_LINE1, "Value"),
            'service_invoice_form': self.fun.get_element_property_sp(main_window, self.fun.loc.INVOICE_LINE1, "Value"),
            'service_client_form': self.fun.get_element_property_sp(main_window, self.fun.loc.CLIENT_LINE1, "Value"),
            'service_buyer_form': self.fun.get_element_property_sp(main_window, self.fun.loc.BUYER_LINE1, "Value"),
            'service_supplier_form': self.fun.get_element_property_sp(main_window, self.fun.loc.SUPPLIER_LINE1, "Value"),
            'service_currency_form': self.fun.get_element_property_sp(main_window, self.fun.loc.CURRENCY_LINE1, "Value"),
            'service_amount_form': self.fun.get_element_property_sp(main_window, self.fun.loc.AMOUNT_LINE1, "Value"),
            'service_info_form': self.fun.get_element_property_sp(main_window, self.fun.loc.INFO_LINE1, "Value"),
            'service_closed_form': self.fun.get_element_property_sp(main_window, self.fun.loc.CLOSED_LINE1, "Value"),
            'service_unpaid_form': self.fun.get_element_property_sp(main_window, self.fun.loc.UNPAID_LINE1, "Value"),
            'service_charged_form': self.fun.get_element_property_sp(main_window, self.fun.loc.CHARGED_LINE1, "Value"),
            'service_charged_sv_form': self.fun.get_element_property_sp(main_window, self.fun.loc.CHARGED_SV_LINE1, "Value"),

        })
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.TAB_SERVICES)
        self.fun.check_element_disappeared(main_window, self.loc.ADD_BUTTON)
        self.fun.check_element_disappeared(main_window, self.loc.ADD_FROM_ORDER_BUTTON)
        self.fun.check_element_disappeared(main_window, self.loc.QUICK_CREATE_MENU)

        # Связываем с Вх. переводы
        self.fun.click_element_sp(main_window, self.loc.INCOMING_TRANSFERS)
        self.fun.click_element_sp(main_window, self.loc.CONNECT_TRANSFERS)
        time.sleep(2)
        self.fun.click_element_sp(main_window, self.loc.SERVICES_OPTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        time.sleep(2)
        self.fun.click_element(main_window, self.loc.EXPAND, timeout=1)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        self.fun.click_element_sp(main_window, self.loc.ADD_SERVICES)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=2)
        time.sleep(2)
        self.fun.order_data.update({
            'service_is_payment_vp': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_PAYMENT_LINE1, "Value"),
            'service_date_vp': self.fun.get_element_property_sp(main_window, self.fun.loc.DATE_LINE1, "Value"),
            'service_is_type_vp': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_TYPE_LINE1, "Value"),
            'service_supplier_vp': self.fun.get_element_property_sp(main_window, self.fun.loc.SUPPLIER_LINE1, "Value"),
            'service_invoice_vp': self.fun.get_element_property_sp(main_window, self.fun.loc.INVOICE_LINE1, "Value"),
            'service_client_vp': self.fun.get_element_property_sp(main_window, self.fun.loc.CLIENT_LINE1, "Value"),
            'service_contractor_vp': self.fun.get_element_property_sp(main_window, self.fun.loc.CONTRACTOR_LINE1, "Value"),
            'service_buyer_vp': self.fun.get_element_property_sp(main_window, self.fun.loc.BUYER_LINE1, "Value"),
            'service_currency_vp': self.fun.get_element_property_sp(main_window, self.fun.loc.CURRENCY_LINE1, "Value"),
            'service_amount_vp': self.fun.get_element_property_sp(main_window, self.fun.loc.AMOUNT_LINE1, "Value"),
            'service_unallocated_vp': self.fun.get_element_property_sp(main_window, self.fun.loc.UNALLOCATED_LINE1, "Value"),
            'service_note_vp': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE_LINE1, "Value"),
            'service_info_vp': self.fun.get_element_property_sp(main_window, self.fun.loc.INFO_LINE1, "Value"),
            'service_closed_vp': self.fun.get_element_property_sp(main_window, self.fun.loc.CLOSED_LINE1, "Value"),
            'service_unpaid_vp': self.fun.get_element_property_sp(main_window, self.fun.loc.UNPAID_LINE1, "Value"),
            'service_charged_vp': self.fun.get_element_property_sp(main_window, self.fun.loc.CHARGED_LINE1, "Value"),
            'service_charged_sv_vp': self.fun.get_element_property_sp(main_window, self.fun.loc.CHARGED_SV_LINE1, "Value"),

        })
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)
        time.sleep(1)
        self.fun.order_data.update({
            'service_is_payment_vp_form': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_PAYMENT_LINE1,
                                                                      "Value"),
            'service_date_vp_form': self.fun.get_element_property_sp(main_window, self.fun.loc.DATE_LINE1, "Value"),
            'service_is_type_vp_form': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_TYPE_LINE1, "Value"),
            'service_supplier_vp_form': self.fun.get_element_property_sp(main_window, self.fun.loc.SUPPLIER_LINE1, "Value"),
            'service_invoice_vp_form': self.fun.get_element_property_sp(main_window, self.fun.loc.INVOICE_LINE1, "Value"),
            'service_client_vp_form': self.fun.get_element_property_sp(main_window, self.fun.loc.CLIENT_LINE1, "Value"),
            'service_contractor_vp_form': self.fun.get_element_property_sp(main_window, self.fun.loc.CONTRACTOR_LINE1,
                                                                      "Value"),
            'service_buyer_vp_form': self.fun.get_element_property_sp(main_window, self.fun.loc.BUYER_LINE1, "Value"),
            'service_currency_vp_form': self.fun.get_element_property_sp(main_window, self.fun.loc.CURRENCY_LINE1, "Value"),
            'service_amount_vp_form': self.fun.get_element_property_sp(main_window, self.fun.loc.AMOUNT_LINE1, "Value"),
            'service_unallocated_vp_form': self.fun.get_element_property_sp(main_window, self.fun.loc.UNALLOCATED_LINE1,
                                                                       "Value"),
            'service_note_vp_form': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE_LINE1, "Value"),
            'service_info_vp_form': self.fun.get_element_property_sp(main_window, self.fun.loc.INFO_LINE1, "Value"),
            'service_closed_vp_form': self.fun.get_element_property_sp(main_window, self.fun.loc.CLOSED_LINE1, "Value"),
            'service_unpaid_vp_form': self.fun.get_element_property_sp(main_window, self.fun.loc.UNPAID_LINE1, "Value"),
            'service_charged_vp_form': self.fun.get_element_property_sp(main_window, self.fun.loc.CHARGED_LINE1, "Value"),
            'service_charged_sv_vp_form': self.fun.get_element_property_sp(main_window, self.fun.loc.CHARGED_SV_LINE1,
                                                                      "Value"),

        })
        # Связываем с Вх. счета
        self.fun.click_element_sp(main_window, self.loc.INCOMING_INVOICES1)
        self.fun.click_element_sp(main_window, self.loc.CONNECT_INVOICES)
        time.sleep(2)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_2)
        self.fun.click_element_sp(main_window, self.loc.ADD_SERVICES)
        self.fun.click_element(main_window, self.loc.EXPAND, timeout=1)
        self.fun.order_data.update({
            'created_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.CREATED_LINE1, "Value"),
            'created_by_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.CREATED_BY_LINE1, "Value"),
            'modified_by_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.MODIFIED_BY_LINE1, "Value"),
            'is_payment_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_PAYMENT_LINE1_1, "Value"),
            'service_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_LINE_01, "Value"),
            'service_date_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.DATE_LINE1, "Value"),
            'account_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.ACCOUNT_LINE1, "Value"),
            'buyer_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.BUYER_LINE1, "Value"),
            'gtd_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.GTD_LINE1, "Value"),
            'feeder_vessel_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.FEEDER_VESSEL_LINE1,
                                                                   "Value"),
            'supplier_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.SUPPLIER_LINE1, "Value"),
            'currency_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.CURRENCY_LINE1, "Value"),
            'amount_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.AMOUNT_LINE1, "Value"),
            'unallocated_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.UNALLOCATED_LINE1, "Value"),
            'info_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.INFO_LINE1, "Value"),
            'note_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE_LINE1, "Value"),
            'linked_is_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.LINKED_IS_LINE1, "Value"),
            'linked_vs_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.LINKED_VS_LINE1, "Value"),
            'client_vs': self.fun.get_element_property_sp(main_window, self.fun.loc.CLIENT_LINE1, "Value"),

        })

        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)
        self.fun.order_data.update({
            'created_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.CREATED_LINE1, "Value"),
            'created_by_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.CREATED_BY_LINE1, "Value"),
            'modified_by_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.MODIFIED_BY_LINE1, "Value"),
            'is_payment_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_PAYMENT_LINE1_1, "Value"),
            'service_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.SERVICE_LINE_01, "Value"),
            'service_date_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.DATE_LINE1, "Value"),
            'account_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.ACCOUNT_LINE1, "Value"),
            'buyer_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.BUYER_LINE1, "Value"),
            'gtd_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.GTD_LINE1, "Value"),
            'feeder_vessel_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.FEEDER_VESSEL_LINE1,
                                                                   "Value"),
            'supplier_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.SUPPLIER_LINE1, "Value"),
            'currency_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.CURRENCY_LINE1, "Value"),
            'amount_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.AMOUNT_LINE1, "Value"),
            'unallocated_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.UNALLOCATED_LINE1, "Value"),
            'info_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.INFO_LINE1, "Value"),
            'note_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.NOTE_LINE1, "Value"),
            'linked_is_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.LINKED_IS_LINE1, "Value"),
            'linked_vs_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.LINKED_VS_LINE1, "Value"),
            'client_vs_form': self.fun.get_element_property_sp(main_window, self.fun.loc.CLIENT_LINE1, "Value"),

        })

        time.sleep(1)

        # Связь с прямыми счетами на клиента
        self.fun.click_element_sp(main_window, self.loc.DIRECT_CLIENT_INVOICES)
        self.fun.click_element_sp(main_window, self.loc.CONNECT_ACCOUNTS_CLIENT)
        time.sleep(2)
        self.fun.click_element(main_window, self.loc.RECIPIENT_1, timeout=1)
        time.sleep(1)
        self.fun.click_element(main_window, self.loc.ADD_SERVICES, timeout=1)
        self.fun.click_element(main_window, self.loc.OK_BUTTON, timeout=1)
        # Сброс настроек
        self.fun.right_click_element(main_window, self.loc.TYPE_IS_TABLE, timeout=3)
        keyboard.send_keys('{DOWN}' * 17)
        keyboard.send_keys('{ENTER}')
        time.sleep(1)
        self.fun.order_data.update({
            'is_type_ps': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_TYPE_LINE1, "Value"),
            'created_by_ps': self.fun.get_element_property(main_window, self.fun.loc.CREATED_BY_LINE1, "Value"),
            'date_ps': self.fun.get_element_property_sp(main_window, self.fun.loc.DATE_LINE1, "Value"),
            'account_ps': self.fun.get_element_property_sp(main_window, self.fun.loc.ACCOUNT_LINE1, "Value"),
            'buyer_ps': self.fun.get_element_property_sp(main_window, self.fun.loc.BUYER_LINE1, "Value"),
            'supplier_ps': self.fun.get_element_property_sp(main_window, self.fun.loc.SUPPLIER_LINE1, "Value"),
            'currency_ps': self.fun.get_element_property_sp(main_window, self.fun.loc.CURRENCY_LINE1, "Value"),
            'amount_ps': self.fun.get_element_property_sp(main_window, self.fun.loc.AMOUNT_LINE1, "Value"),
            'info_ps': self.fun.get_element_property_sp(main_window, self.fun.loc.INFO_LINE1, "Value"),

        })
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)
        time.sleep(2)
        self.fun.right_click_element(main_window, self.loc.CHECK_TABLE, timeout=3)
        keyboard.send_keys('{DOWN}' * 18)
        keyboard.send_keys('{ENTER}')
        self.fun.order_data.update({
            'is_type_ps_form': self.fun.get_element_property_sp(main_window, self.fun.loc.IS_TYPE_LINE1, "Value"),
            'created_by_ps_form': self.fun.get_element_property_sp(main_window, self.fun.loc.CREATED_BY_LINE1, "Value"),
            'date_ps_form': self.fun.get_element_property_sp(main_window, self.fun.loc.DATE_LINE1, "Value"),
            'account_ps_form': self.fun.get_element_property_sp(main_window, self.fun.loc.ACCOUNT_LINE1, "Value"),
            'buyer_ps_form': self.fun.get_element_property_sp(main_window, self.fun.loc.BUYER_LINE1, "Value"),
            'supplier_ps_form': self.fun.get_element_property_sp(main_window, self.fun.loc.SUPPLIER_LINE1, "Value"),
            'currency_ps_form': self.fun.get_element_property_sp(main_window, self.fun.loc.CURRENCY_LINE1, "Value"),
            'amount_ps_form': self.fun.get_element_property_sp(main_window, self.fun.loc.AMOUNT_LINE1, "Value"),
            'info_ps_form': self.fun.get_element_property_sp(main_window, self.fun.loc.INFO_LINE1, "Value"),

        })
        self.fun.click_element_sp(main_window, self.loc.APPLY_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)

        time.sleep(1)

        # Связываем с Взаимозачеты с вх. счетами
        self.fun.click_element_sp(main_window, self.loc.OFFSETS)
        self.fun.click_element_sp(main_window, self.loc.CONNECT_OFFSETS)
        self.fun.click_element_sp(main_window, self.loc.SERVICES_OPTIONS)
        keyboard.send_keys('{DOWN}')
        keyboard.send_keys('{ENTER}')
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.RECIPIENT_1)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.ADD_SERVICES)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)

        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.RELATIONS)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.PENALTY_INVOICES)
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.FILES)
        time.sleep(1)

        # Синхронизация счета с 1С

        self.fun.click_element_sp(main_window, self.loc.TAB_CHECK1)
        self.fun.click_element_sp(main_window, self.loc.SYNC_BUTTON_1C)
        time.sleep(3)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)
        time.sleep(2)

        #self.fun.order_data.update({
        #   'is_sync_ок': self.fun.get_element_property_sp(main_window, self.fun.loc.SYNC_1C, "Value"),
        #})

        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON) #Не работает синхронизация
        time.sleep(1)
        self.fun.click_element_sp(main_window, self.loc.OK_BUTTON1)

        # таблица Все счета
        main_window = self.fun.get_main_window()
        main_window.set_focus()
        time.sleep(2)
        self.fun.click_element_sp(main_window, self.loc.MENU_BAZA)
        keyboard.send_keys('{DOWN 3}')
        keyboard.send_keys('{ENTER}')
        time.sleep(1)
        keyboard.send_keys('{ENTER}')
        time.sleep(2)

        self.fun.click_element_sp(main_window, self.loc.INVOICES_FILTER)
        keyboard.send_keys(text, with_spaces=True)
        keyboard.send_keys('{ENTER}')
        self.fun.order_data.update({
            'data_all_accounts': self.fun.get_element_property_sp(main_window, self.loc.DATE_LINE1, "Value"),
            'supplier_all_accounts': self.fun.get_element_property_sp(main_window, self.loc.SUPPLIER_LINE1, "Value"),
            'account_all_accounts': self.fun.get_element_property_sp(main_window, self.loc.ACCOUNT_LINE1, "Value"),
            'client_all_accounts': self.fun.get_element_property_sp(main_window, self.loc.CLIENT_LINE1, "Value"),
            'buyer_all_accounts': self.fun.get_element_property_sp(main_window, self.loc.BUYER_LINE1, "Value"),
            'currency_all_accounts': self.fun.get_element_property_sp(main_window, self.loc.CURRENCY_LINE1, "Value"),
            'amount_all_accounts': self.fun.get_element_property_sp(main_window, self.loc.AMOUNT_LINE1, "Value"),
            'closed_all_accounts': self.fun.get_element_property_sp(main_window, self.loc.CLOSED_LINE1, "Value"),
            'unpaid_all_accounts': self.fun.get_element_property_sp(main_window, self.loc.UNPAID_LINE1, "Value"),
            'note_all_accounts': self.fun.get_element_property_sp(main_window, self.loc.NOTE_LINE1, "Value")
        })

        # таблица Все услуги
        self.fun.click_element_sp(main_window, self.loc.MENU_BAZA)
        keyboard.send_keys('{DOWN 3}')
        keyboard.send_keys('{ENTER}')
        keyboard.send_keys('{DOWN 13}')
        keyboard.send_keys('{ENTER}')
        time.sleep(2)
        self.fun.click_element_sp(main_window, self.loc.INVOICES_FILTER1)
        keyboard.send_keys(text, with_spaces=True)
        keyboard.send_keys('{ENTER}')
        self.fun.order_data.update({
            'all_serv_invoice_number': self.fun.get_element_property_sp(main_window, self.loc.INVOICE_NUMBER_1, "Value"),
            'all_serv_invoice_date': self.fun.get_element_property_sp(main_window, self.loc.INVOICE_DATE_1, "Value"),
            'all_serv_service': self.fun.get_element_property_sp(main_window, self.loc.SERVICE_LINE1, "Value"),
            'all_serv_client': self.fun.get_element_property_sp(main_window, self.loc.CLIENT_LINE1, "Value"),
            'all_serv_buyer': self.fun.get_element_property_sp(main_window, self.loc.BUYER_LINE1, "Value"),
            'all_serv_supplier': self.fun.get_element_property_sp(main_window, self.loc.SUPPLIER_LINE1, "Value"),
            'all_serv_rate': self.fun.get_element_property_sp(main_window, self.loc.RATE_LINE1, "Value"),
            'all_serv_currency': self.fun.get_element_property_sp(main_window, self.loc.CURRENCY_LINE1, "Value"),
            'all_serv_quantity': self.fun.get_element_property_sp(main_window, self.loc.QUANTITY_LINE1, "Value"),
            'all_serv_invoice_note': self.fun.get_element_property_sp(main_window, self.loc.INVOICE_NOTE_1, "Value")
        })
        time.sleep(10)

        return self.fun.order_data

    def close(self):
        """Завершение работы приложения"""
        self.fun.app.kill(soft=True)