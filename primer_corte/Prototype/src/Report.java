// Prototipo concreto: Reporte
class Report extends AbstractDocument {
    private String reportData;
    private String department;
    private int numberOfPages;
    
    public Report() {
    }
    
    // Constructor prototipo
    public Report(Report source) {
        // Llamar al constructor padre para copiar los campos de la clase padre
        super(source);
        if (source != null) {
            this.reportData = source.reportData;
            this.department = source.department;
            this.numberOfPages = source.numberOfPages;
        }
    }
    
    // Getters y setters
    public String getReportData() {
        return reportData;
    }
    
    public void setReportData(String reportData) {
        this.reportData = reportData;
    }
    
    public String getDepartment() {
        return department;
    }
    
    public void setDepartment(String department) {
        this.department = department;
    }
    
    public int getNumberOfPages() {
        return numberOfPages;
    }
    
    public void setNumberOfPages(int numberOfPages) {
        this.numberOfPages = numberOfPages;
    }
    
    @Override
    public Document clone() {
        return new Report(this);
    }
    
    @Override
    public void print() {
        System.out.println("---- REPORT ----");
        System.out.println("Title: " + getTitle());
        System.out.println("Author: " + getAuthor());
        System.out.println("Creation Date: " + getCreationDate());
        System.out.println("Department: " + department);
        System.out.println("Pages: " + numberOfPages);
        System.out.println("Data: " + reportData);
    }
    
    @Override
    public String toString() {
        return "Report [title=" + getTitle() + ", author=" + getAuthor() + 
               ", department=" + department + ", pages=" + numberOfPages + "]";
    }
}