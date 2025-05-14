from abstract_document import AbstractDocument

# Prototipo concreto: Email
class Email(AbstractDocument):
    def __init__(self, source=None):
        self.recipients = None
        self.subject = None
        self.body = None
        self.has_attachments = False
        
        # Inicializar atributos de la clase padre
        super().__init__()
        
        # Si se proporciona una fuente, copiar sus atributos
        if source:
            self.__init_copy__(source)
            self.recipients = source.recipients
            self.subject = source.subject
            self.body = source.body
            self.has_attachments = source.has_attachments

    # Getters y setters
    def get_recipients(self):
        return self.recipients

    def set_recipients(self, recipients):
        self.recipients = recipients

    def get_subject(self):
        return self.subject

    def set_subject(self, subject):
        self.subject = subject

    def get_body(self):
        return self.body

    def set_body(self, body):
        self.body = body

    def is_has_attachments(self):
        return self.has_attachments

    def set_has_attachments(self, has_attachments):
        self.has_attachments = has_attachments

    def clone(self):
        return Email(self)

    def print(self):
        print("---- EMAIL ----")
        print(f"Titulo: {self.get_title()}")
        print(f"Autor: {self.get_author()}")
        print(f"Fecha de creacion: {self.get_creation_date()}")
        print(f"Para: {self.recipients}")
        print(f"Asunto: {self.subject}")
        print(f"Cuerpo: {self.body}")
        print(f"Anexos: {'Yes' if self.has_attachments else 'No'}")
        print("--------------")

    def __str__(self):
        return f"Email [title={self.get_title()}, subject={self.subject}, " \
               f"recipients={self.recipients}, hasAttachments={self.has_attachments}]"
