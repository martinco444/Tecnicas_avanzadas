// Registro de documentos (opcional)
class DocumentRegistry {
    private static final java.util.Map<String, Document> DOCUMENT_CACHE = new java.util.HashMap<>();
    
    static {
        // Inicializar con algunos prototipos predefinidos
        Report monthlyReport = new Report();
        monthlyReport.setTitle("Monthly Report Template");
        monthlyReport.setAuthor("System");
        monthlyReport.setCreationDate("2025-03-01");
        monthlyReport.setDepartment("All Departments");
        monthlyReport.setNumberOfPages(5);
        monthlyReport.setReportData("<<Insert monthly data here>>");
        DOCUMENT_CACHE.put("monthlyReportTemplate", monthlyReport);
        
        Email meetingInvitation = new Email();
        meetingInvitation.setTitle("Meeting Invitation Template");
        meetingInvitation.setAuthor("System");
        meetingInvitation.setCreationDate("2025-03-01");
        meetingInvitation.setRecipients("<<Recipients>>");
        meetingInvitation.setSubject("Meeting Invitation: <<Topic>>");
        meetingInvitation.setBody("Dear team,\n\nPlease join us for a meeting about <<Topic>> on <<Date>> at <<Time>>.\n\nBest regards,\n<<Your Name>>");
        meetingInvitation.setHasAttachments(false);
        DOCUMENT_CACHE.put("meetingInvitationTemplate", meetingInvitation);
    }
    
    public static Document getDocument(String documentId) {
        Document cachedDocument = DOCUMENT_CACHE.get(documentId);
        if (cachedDocument != null) {
            return cachedDocument.clone();
        }
        return null;
    }
    
    // Método para añadir nuevos prototipos al registro
    public static void addDocument(String documentId, Document document) {
        DOCUMENT_CACHE.put(documentId, document);
    }
}


