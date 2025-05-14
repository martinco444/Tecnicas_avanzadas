from document_registry import DocumentRegistry
from email import Email
from report import Report


# Clase cliente que utiliza el patrón Prototype
def main():
    # Uso básico del patrón Prototype
    print("===== CREACIÓN DIRECTA DE DOCUMENTOS =====")

    firstReport = Report()
    firstReport.set_title("Reporte Financiero 2025-1")
    firstReport.set_author("Pedro Perez")
    firstReport.set_creation_date("2025-03-20")
    firstReport.set_department("Finanzas")
    firstReport.set_number_of_pages(12)
    firstReport.set_report_data("Informacion de finanzas del primer periodo del 2025...")

    # Clonar el reporte para crear una versión editable
    editable_report = firstReport.clone()

    print("Reporte Original: ")
    firstReport.print()

    print("\nReporte clonado: ")
    editable_report.print()

    #Son iguales los reportes?
    print(f"Son iguales los reportes?: {firstReport==editable_report}")

    #Podemmos editar el clon
    editable_report.set_title("Reporte Financiero 2025-1 (Draft)")
    editable_report.set_author("Pedro Perez y Maria Lopez")

    print("\nReporte clonado (Edited): ")
    editable_report.print()

    # Crear un correo electrónico
    team_email = Email()
    team_email.set_title("Actualizacion Proyecto")
    team_email.set_author("Gerente")
    team_email.set_creation_date("2025-03-17")
    team_email.set_recipients("equipo@empresa.com")
    team_email.set_subject("WActualizacion semana")
    team_email.set_body("Esta es la actualizacion de logros semanales...")
    team_email.set_has_attachments(False)


    # Clonar el correo para múltiples departamentos
    marketing_email = team_email.clone()
    marketing_email.set_recipients("marketing@company.com")
    marketing_email.set_body("Esta es la actualizacion de logros semanales para el departamento de Marketing...")

    sales_email = team_email.clone()
    sales_email.set_recipients("sales@company.com")
    sales_email.set_body("Esta es la actualizacion de logros semanales para el departamento de ventas...")

    print("\nEmail Original: ")
    team_email.print()

    print("\nEmail Clonado (Marketing): ")
    marketing_email.print()

    print("\nEmail Clonado (Sales): ")
    sales_email.print()

    # Uso del registro de documentos
    print("\n===== USO DEL REGISTRO DE DOCUMENTOS =====")

    # Obtener plantillas del registro
    monthly_report_template = DocumentRegistry.get_document("reporteMensualTemplate")
    meeting_invitation_template = DocumentRegistry.get_document("invitacionReunionTemplate")

    # Personalizar las plantillas
    if monthly_report_template:
        monthly_report_template.set_title("Marzo 2025 Reporte de Marketing")
        monthly_report_template.set_author("Maria Lopez")
        monthly_report_template.set_department("Marketing")
        monthly_report_template.set_report_data("Informacion del departamento de Marketing para marzo del 2025...")

        print("Reporte mensual del Template:")
        monthly_report_template.print()

    if meeting_invitation_template:
        meeting_invitation_template.set_author("Juan Lopez")
        meeting_invitation_template.set_recipients("team@company.com")
        meeting_invitation_template.set_subject("Invitacion de reunion:Planeacion")
        
        body = meeting_invitation_template.get_body()
        body = body.replace("<<Topic>>", "Planeacion")
        body = body.replace("<<Date>>", "Marzo 25, 2025")
        body = body.replace("<<Time>>", "10:00 AM")
        body = body.replace("<<Your Name>>", "Juan Lopez")
        meeting_invitation_template.set_body(body)

        print("\nInvitacion de Reunion del Template: ")
        meeting_invitation_template.print()

    # Agregar un nuevo prototipo personalizado al registro
    project_proposal_template = Report()
    project_proposal_template.set_title("Propuesta de Proyecto Template")
    project_proposal_template.set_author("Oficina")
    project_proposal_template.set_creation_date("2025-03-17")
    project_proposal_template.set_department("Todos Deoartamentos")
    project_proposal_template.set_number_of_pages(8)
    project_proposal_template.set_report_data("1. Problematica\n2. Objetivos\n3. Tiempos\n4. Recursos\n5. Presuspuesto")

    DocumentRegistry.add_document("projectProposalTemplate", project_proposal_template)

    # Recuperar y personalizar el nuevo prototipo
    new_project_proposal = DocumentRegistry.get_document("projectProposalTemplate")
    if new_project_proposal:
        new_project_proposal.set_title("Implementacion Propuesta de Proyecto")
        new_project_proposal.set_author("Equipo de tecnologia")
        new_project_proposal.set_department("IT")

        print("\nNueva propuesta de proyecto del Template: ")
        new_project_proposal.print()


if __name__ == "__main__":
    main()

