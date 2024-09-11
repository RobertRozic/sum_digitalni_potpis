from pyhanko.sign.fields import SigFieldSpec, append_signature_field
from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign.signers import SimpleSigner, PdfSigner, PdfSignatureMetadata

signer = SimpleSigner.load_pkcs12(
    pfx_file='certificate.p12',
    passphrase=b'sum123'
)

with open("diploma.pdf", "rb") as doc:
    writer = IncrementalPdfFileWriter(doc)
    append_signature_field(writer, SigFieldSpec(sig_field_name="Signature1"))
    with open("signed_diploma.pdf", "wb") as signed_pdf_file:
        PdfSigner(
            signature_meta=PdfSignatureMetadata(field_name="Signature1"),
            signer=signer
        ).sign_pdf(writer, output=signed_pdf_file)
