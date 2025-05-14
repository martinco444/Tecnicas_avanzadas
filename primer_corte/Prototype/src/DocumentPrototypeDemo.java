// Clase cliente que utiliza el patrón Prototype
public class DocumentPrototypeDemo {
    public static void main(String[] args) {
        // Uso básico del patrón Prototype
        System.out.println("===== CREACIÓN DIRECTA DE DOCUMENTOS =====");
        
        Report firstReport = new Report();
        firstReport.setTitle("Reporte Financiero 2025-1");
        firstReport.setAuthor("Pedro Perez");
        firstReport.setCreationDate("2025-03-20");
        firstReport.setDepartment("Finanzas");
        firstReport.setNumberOfPages(12);
        firstReport.setReportData("Informacion de finanzas del primer periodo del 2025...");
        
        // Clonar el reporte para crear una versión editable
        Report editableReport = (Report) firstReport.clone();

        System.out.println("Reporte Original: ");
        firstReport.print();
        
        System.out.println("\nReporte clonado: ");
        editableReport.print();

        //Son iguales los objetos clonados? 
        boolean sonIguales = firstReport==editableReport;
        System.out.println("\nSon iguales los objetos clonados?  "+sonIguales);

        editableReport.setTitle("Reporte Financiero 2025-1 (Draft)");
        editableReport.setAuthor("Pedro Perez y Maria Lopez");
        
        System.out.println("\nReporte clonado (editado): ");
        editableReport.print();
        
        // Crear un correo electrónico
        Email teamEmail = new Email();
        teamEmail.setTitle("Actualizacion Proyecto");
        teamEmail.setAuthor("Gerente");
        teamEmail.setCreationDate("2025-03-17");
        teamEmail.setRecipients("equipo@empresa.com");
        teamEmail.setSubject("Actualizacion semanal");
        teamEmail.setBody("Esta es la actualizacion de logros semanales...");
        teamEmail.setHasAttachments(false);
        
        // Clonar el correo para múltiples departamentos
        Email marketingEmail = (Email) teamEmail.clone();
        marketingEmail.setRecipients("marketing@company.com");
        marketingEmail.setBody("Esta es la actualizacion de logros semanales para el departamento de Marketing...");
        
        Email salesEmail = (Email) teamEmail.clone();
        salesEmail.setRecipients("sales@company.com");
        salesEmail.setBody("Esta es la actualizacion de logros semanales para el departamento de ventas...");
        
        System.out.println("\nEmail original: ");
        teamEmail.print();
        
        System.out.println("\nEmail clonado(Marketing): ");
        marketingEmail.print();
        
        System.out.println("\nEmail clonado(Ventas): ");
        salesEmail.print();
        
        // Uso del registro de documentos
        System.out.println("\nUSO DEL REGISTRO DE DOCUMENTOS");
        
        // Obtener plantillas del registro
        Report monthlyReportTemplate = (Report) DocumentRegistry.getDocument("reporteMensualTemplate");
        Email meetingInvitationTemplate = (Email) DocumentRegistry.getDocument("invitacionReunionTemplate");
        
        // Personalizar las plantillas
        if (monthlyReportTemplate != null) {
            monthlyReportTemplate.setTitle("Marzo 2025 Reporte de Marketing");
            monthlyReportTemplate.setAuthor("Maria Lopez");
            monthlyReportTemplate.setDepartment("Marketing");
            monthlyReportTemplate.setReportData("Informacion del departamento de Marketing para marzo del 2025...");
            
            System.out.println("Reporte mensual del Template: ");
            monthlyReportTemplate.print();
        }
        
        if (meetingInvitationTemplate != null) {
            meetingInvitationTemplate.setAuthor("Juan Lopez");
            meetingInvitationTemplate.setRecipients("team@company.com");
            meetingInvitationTemplate.setSubject("Invitacion de reunion:Planeacion");
            meetingInvitationTemplate.setBody(meetingInvitationTemplate.getBody()
                    .replace("<<Topic>>", "Planeacion")
                    .replace("<<Date>>", "Marzo 25, 2025")
                    .replace("<<Time>>", "10:00 AM")
                    .replace("<<Your Name>>", "Juan Lopez"));
            
            System.out.println("\nInvitacion de Reunion del Template: ");
            meetingInvitationTemplate.print();
        }
        
        // Agregar un nuevo prototipo personalizado al registro
        Report projectProposalTemplate = new Report();
        projectProposalTemplate.setTitle("Propuesta de Proyecto Template");
        projectProposalTemplate.setAuthor("Oficina");
        projectProposalTemplate.setCreationDate("2025-03-17");
        projectProposalTemplate.setDepartment("Todos Deoartamentos");
        projectProposalTemplate.setNumberOfPages(8);
        projectProposalTemplate.setReportData("1. Problematica\n2. Objetivos\n3. Tiempos\n4. Recursos\n5. Presuspuesto");
        
        DocumentRegistry.addDocument("projectProposalTemplate", projectProposalTemplate);
        
        // Recuperar y personalizar el nuevo prototipo
        Report newProjectProposal = (Report) DocumentRegistry.getDocument("projectProposalTemplate");
        if (newProjectProposal != null) {
            newProjectProposal.setTitle("Implementacion Propuesta de Proyecto");
            newProjectProposal.setAuthor("Equipo de tecnologia");
            newProjectProposal.setDepartment("IT");
            
            System.out.println("\nNuevo proyecto del Template: ");
            newProjectProposal.print();
        }
    }
}