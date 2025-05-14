// Prototipo concreto: Email
class Email extends AbstractDocument {
    private String recipients;
    private String subject;
    private String body;
    private boolean hasAttachments;
    
    public Email() {
    }
    
    // Constructor prototipo
    public Email(Email source) {
        // Llamar al constructor padre para copiar los campos de la clase padre
        super(source);
        if (source != null) {
            this.recipients = source.recipients;
            this.subject = source.subject;
            this.body = source.body;
            this.hasAttachments = source.hasAttachments;
        }
    }
    
    // Getters y setters
    public String getRecipients() {
        return recipients;
    }
    
    public void setRecipients(String recipients) {
        this.recipients = recipients;
    }
    
    public String getSubject() {
        return subject;
    }
    
    public void setSubject(String subject) {
        this.subject = subject;
    }
    
    public String getBody() {
        return body;
    }
    
    public void setBody(String body) {
        this.body = body;
    }
    
    public boolean isHasAttachments() {
        return hasAttachments;
    }
    
    public void setHasAttachments(boolean hasAttachments) {
        this.hasAttachments = hasAttachments;
    }
    
    @Override
    public Document clone() {
        return new Email(this);
    }
    
    @Override
    public void print() {
        System.out.println("---- EMAIL ----");
        System.out.println("Title: " + getTitle());
        System.out.println("Author: " + getAuthor());
        System.out.println("Creation Date: " + getCreationDate());
        System.out.println("To: " + recipients);
        System.out.println("Subject: " + subject);
        System.out.println("Body: " + body);
        System.out.println("Has Attachments: " + (hasAttachments ? "Yes" : "No"));
    }
    
    @Override
    public String toString() {
        return "Email [title=" + getTitle() + ", subject=" + subject + 
               ", recipients=" + recipients + ", hasAttachments=" + hasAttachments + "]";
    }
}