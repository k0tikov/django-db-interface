import xlsxwriter
from io import StringIO, BytesIO
from django.utils.translation import ugettext
from .models import List_of_regedit_buy

# Creatin Excel data for exporting
def writeToExcel(take_data):
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet('Summary')
    # Excel styles
    title = workbook.add_format({
        'bg_color': '#F0F4FF',
        'bold': True,
        'font_size': 13,
        'align': 'center',
        'valign': 'vcenter',
        'border': 1
    })
    header = workbook.add_format({
        'bg_color': '#F7F7F7',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
    })
    # Rows and columns
    row = 1
    column = 0
    # Column widths
    col_width = 10
    onec_code_col_width = 15
    name_of_buyer_col_width = 30
    theme_of_contract_col_width = 25
    number_col_width = 20
    date_of_contract_col_width = 17
    expiration_col_width = 26
    total_col_width = 18
    comments_col_width = 25
    technical_col_width = 15
    tags_col_width = 10
    status_col_width = 15
    subcontractor_col_width = 15
    check_number_col_width = 30
    # Create header
    worksheet.write(0, 0, ugettext('Год'), title)
    worksheet.write(0, 1, ugettext('Наименование поставщика'), title)
    worksheet.write(0, 2, ugettext('Предмет договора'), title)
    worksheet.write(0, 3, ugettext('Номер'), title)
    worksheet.write(0, 4, ugettext('Код в 1С'), title)
    worksheet.write(0, 5, ugettext('Дата договора'), title)
    worksheet.write(0, 6, ugettext('Срок действия договора'), title)
    worksheet.write(0, 7, ugettext('Сумма договора'), title)
    worksheet.write(0, 8, ugettext('Комментарии'), title)
    worksheet.write(0, 9, ugettext('Техописание'), title)
    worksheet.write(0, 10, ugettext('Теги'), title)
    worksheet.write(0, 11, ugettext('Статус'), title)
    worksheet.write(0, 12, ugettext('Подрядчик'), title)
    worksheet.write(0, 13, ugettext('№ договора с подрядчиком'), title)  
    # Add data to the table
    for data in take_data:
        worksheet.write(row, column, data.date_of_completion, header)
           
        worksheet.write(row, column + 1, data.name_of_buyer, header)
        if len(data.name_of_buyer) > name_of_buyer_col_width:
            name_of_buyer_col_width = len(data.name_of_buyer) + 5
            
        worksheet.write(row, column + 2, data.theme_of_contract, header)
        if len(data.theme_of_contract) > theme_of_contract_col_width:
            theme_of_contract_col_width = len(data.theme_of_contract) + 3
            
        worksheet.write(row, column + 3, data.number, header)
        if len(data.number) > number_col_width:
            number_col_width = len(data.number)

        worksheet.write(row, column + 4, data.onec_code, header)
        if len(data.onec_code) > onec_code_col_width:
            onec_code_col_width = len(data.onec_code) + 5

        worksheet.write(row, column + 5, data.date_of_contract, header)
        if len(data.date_of_contract) > date_of_contract_col_width:
            date_of_contract_col_width = len(data.date_of_contract)
            
        worksheet.write(row, column + 6, data.expiration, header)
        if len(data.expiration) > expiration_col_width:
            expiration_col_width = len(data.expiration) + 5
        
        worksheet.write(row, column + 7, data.total, header)
        if len(data.total) > total_col_width:
            total_col_width = len(data.total)
        
        worksheet.write(row, column + 8, data.comments, header)
        if len(data.comments) > comments_col_width:
            comments_col_width = len(data.comments) + 5

        worksheet.write(row, column + 9, data.technical, header)
        if len(data.technical) > technical_col_width:
            technical_col_width = len(data.technical) + 5
     
        worksheet.write(row, column + 10, data.tags, header)
        if len(data.tags) > tags_col_width:
            tags_col_width = len(data.tags)
            
        worksheet.write(row, column + 11, data.status, header)
        if len(data.status) > status_col_width:
            status_col_width = len(data.status)
            
        worksheet.write(row, column + 12, data.subcontractor, header)
        if len(data.subcontractor) > subcontractor_col_width:
            subcontractor_col_width = len(data.subcontractor) + 5
            
        worksheet.write(row, column + 13, data.check_number, header)
        if len(data.check_number) > check_number_col_width:
            check_number_col_width = len(data.check_number) + 5
            
        row += 1
    # Change column widths
    worksheet.set_column('A:A', col_width)
    worksheet.set_column('B:B', name_of_buyer_col_width)
    worksheet.set_column('C:C', theme_of_contract_col_width)
    worksheet.set_column('D:D', number_col_width)
    worksheet.set_column('E:E', onec_code_col_width)
    worksheet.set_column('F:F', date_of_contract_col_width)
    worksheet.set_column('G:G', expiration_col_width)
    worksheet.set_column('H:H', total_col_width)
    worksheet.set_column('I:I', comments_col_width)
    worksheet.set_column('J:J', technical_col_width)
    worksheet.set_column('K:K', tags_col_width)
    worksheet.set_column('L:L', status_col_width)
    worksheet.set_column('M:M', subcontractor_col_width)
    worksheet.set_column('N:N', check_number_col_width)  
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data
