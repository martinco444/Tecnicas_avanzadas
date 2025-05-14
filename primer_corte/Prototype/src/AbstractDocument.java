// Clase abstracta que implementa la interfaz Document
abstract class AbstractDocument implements Document {
    private String author;
    private String creationDate;
    private String title;
    
    // Constructor normal
    public AbstractDocument() {
    }
    
    // Constructor prototipo
    public AbstractDocument(AbstractDocument source) {
        if (source != null) {
            this.author = source.author;
            this.creationDate = source.creationDate;
            this.title = source.title;
        }
    }
    
    // Getters y setters
    public String getAuthor() {
        return author;
    }
    
    public void setAuthor(String author) {
        this.author = author;
    }
    
    public String getCreationDate() {
        return creationDate;
    }
    
    public void setCreationDate(String creationDate) {
        this.creationDate = creationDate;
    }
    
    public String getTitle() {
        return title;
    }
    
    public void setTitle(String title) {
        this.title = title;
    }
    
    @Override
    public abstract Document clone();
    
    @Override
    public abstract void print();
}