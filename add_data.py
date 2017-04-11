from app import db, models

'''
dataset = models.Dataset(dir_name="24336569_LanderES_Science_2014", pmid="24336569", journal="Science", year="2014", species="human",
                  initial_condition="HL60_initial,KBM7_initial", cell_line="HL60", type="ko", library="Addgene_51043-8",
                  norm_method="none", treatment="", other_condition="", culture_days="", sample="HL60_initial", is_initial_condition=True,
                  source="counts", first_author="Wang T", last_author="Lander ES",
                  title="Genetic Screens in Human Cells Using the CRISPR-Cas9 System", contact="Yingbo Cui", public_status="public")
db.session.add(dataset)

dataset = models.Dataset(dir_name="24336569_LanderES_Science_2014", pmid="24336569", journal="Science", year="2014", species="human",
                  initial_condition="HL60_initial,KBM7_initial", cell_line="KBM-7", type="ko", library="Addgene_51043-8",
                  norm_method="none", treatment="", other_condition="", culture_days="", sample="KBM7_initial", is_initial_condition=True,
                  source="counts", first_author="Wang T", last_author="Lander ES",
                  title="Genetic Screens in Human Cells Using the CRISPR-Cas9 System", contact="Yingbo Cui", public_status="public")
db.session.add(dataset)

dataset = models.Dataset(dir_name="24336569_LanderES_Science_2014", pmid="24336569", journal="Science", year="2014", species="human",
                  initial_condition="HL60_initial,KBM7_initial", cell_line="HL60", type="ko", library="Addgene_51043-8",
                  norm_method="none", treatment="", other_condition="", culture_days="", sample="HL60_final", is_initial_condition=False,
                  source="counts", first_author="Wang T", last_author="Lander ES",
                  title="Genetic Screens in Human Cells Using the CRISPR-Cas9 System", contact="Yingbo Cui", public_status="public")
db.session.add(dataset)

dataset = models.Dataset(dir_name="24336569_LanderES_Science_2014", pmid="24336569", journal="Science", year="2014", species="human",
                  initial_condition="HL60_initial,KBM7_initial", cell_line="KBM-7", type="ko", library="Addgene_51043-8",
                  norm_method="none", treatment="", other_condition="", culture_days="", sample="KBM7_final", is_initial_condition=False,
                  source="counts", first_author="Wang T", last_author="Lander ES",
                  title="Genetic Screens in Human Cells Using the CRISPR-Cas9 System", contact="Yingbo Cui", public_status="public")
db.session.add(dataset)
'''

dataset = models.Dataset(dir_name="27760321_YusaK_CellRep_2016_1", pmid="27760321", journal="CellRep", year="2016", species="human",
                  initial_condition="HumanV1_1,HumanV1_2", cell_line="HL60", type="ko", library="Addgene_67989",
                  norm_method="350_noness", treatment="", other_condition="", culture_days="", sample="HL60_rep_1", is_initial_condition=False,
                  source="counts", first_author="Tzelepis K", last_author="Yusa K",
                  title="A CRISPR Dropout Screen Identifies Genetic Vulnerabilities and Therapeutic Targets in Acute Myeloid Leukemia", contact="Yingbo Cui", public_status="public")
db.session.add(dataset)

dataset = models.Dataset(dir_name="27760321_YusaK_CellRep_2016_1", pmid="27760321", journal="CellRep", year="2016", species="human",
                  initial_condition="HumanV1_1,HumanV1_2", cell_line="HL60", type="ko", library="Addgene_67989",
                  norm_method="350_noness", treatment="", other_condition="", culture_days="", sample="HL60_rep_2", is_initial_condition=False,
                  source="counts", first_author="Tzelepis K", last_author="Yusa K",
                  title="A CRISPR Dropout Screen Identifies Genetic Vulnerabilities and Therapeutic Targets in Acute Myeloid Leukemia", contact="Yingbo Cui", public_status="public")
db.session.add(dataset)

dataset = models.Dataset(dir_name="26472758_SabatiniDM_Science_2015", pmid="26472758", journal="Science", year="2015", species="human",
                  initial_condition="KBM7_initial_1,KBM7_initial_2,K562_initial,Jiyoye_initial,Raji_initial", cell_line="KBM-7", type="ko", library="Addgene_1000000067",
                  norm_method="350_noness", treatment="", other_condition="", culture_days="", sample="KBM7_initial_1", is_initial_condition=True,
                  source="counts", first_author="Wang T", last_author="Sabatini DM",
                  title="Identification and characterization of essential genes in the human genome", contact="Yingbo Cui", public_status="public")
db.session.add(dataset)

dataset = models.Dataset(dir_name="26472758_SabatiniDM_Science_2015", pmid="26472758", journal="Science", year="2015", species="human",
                  initial_condition="KBM7_initial_1,KBM7_initial_2,K562_initial,Jiyoye_initial,Raji_initial", cell_line="KBM-7", type="ko", library="Addgene_1000000067",
                  norm_method="350_noness", treatment="", other_condition="", culture_days="", sample="KBM7_initial_2", is_initial_condition=True,
                  source="counts", first_author="Wang T", last_author="Sabatini DM",
                  title="Identification and characterization of essential genes in the human genome", contact="Yingbo Cui", public_status="public")
db.session.add(dataset)

dataset = models.Dataset(dir_name="26472758_SabatiniDM_Science_2015", pmid="26472758", journal="Science", year="2015", species="human",
                  initial_condition="KBM7_initial_1,KBM7_initial_2,K562_initial,Jiyoye_initial,Raji_initial", cell_line="KBM-7", type="ko", library="Addgene_1000000067",
                  norm_method="350_noness", treatment="", other_condition="", culture_days="", sample="KBM7_final_1", is_initial_condition=False,
                  source="counts", first_author="Wang T", last_author="Sabatini DM",
                  title="Identification and characterization of essential genes in the human genome", contact="Yingbo Cui", public_status="public")
db.session.add(dataset)

dataset = models.Dataset(dir_name="26472758_SabatiniDM_Science_2015", pmid="26472758", journal="Science", year="2015", species="human",
                  initial_condition="KBM7_initial_1,KBM7_initial_2,K562_initial,Jiyoye_initial,Raji_initial", cell_line="KBM-7", type="ko", library="Addgene_1000000067",
                  norm_method="350_noness", treatment="", other_condition="", culture_days="", sample="KBM7_final_2", is_initial_condition=False,
                  source="counts", first_author="Wang T", last_author="Sabatini DM",
                  title="Identification and characterization of essential genes in the human genome", contact="Yingbo Cui", public_status="public")
db.session.add(dataset)

dataset = models.Dataset(dir_name="26232224_SabatiniDM_Cell_2015", pmid="26232224", journal="Cell", year="2015", species="human",
                  initial_condition="t0", cell_line="Jurkat", type="ko", library="Addgene_1000000067",
                  norm_method="350_noness", treatment="", other_condition="", culture_days="", sample="t0", is_initial_condition=True,
                  source="counts", first_author="Birsoy K", last_author="Sabatini DM",
                  title="An Essential Role of the Mitochondrial Electron Transport Chain in Cell Proliferation Is to Enable Aspartate Synthesis", contact="Yingbo Cui", public_status="public")
db.session.add(dataset)

dataset = models.Dataset(dir_name="26232224_SabatiniDM_Cell_2015", pmid="26232224", journal="Cell", year="2015", species="human",
                  initial_condition="t0", cell_line="Jurkat", type="ko", library="Addgene_1000000067",
                  norm_method="350_noness", treatment="Phenformin", other_condition="", culture_days="", sample="phenformin", is_initial_condition=False,
                  source="counts", first_author="Birsoy K", last_author="Sabatini DM",
                  title="An Essential Role of the Mitochondrial Electron Transport Chain in Cell Proliferation Is to Enable Aspartate Synthesis", contact="Yingbo Cui", public_status="public")
db.session.add(dataset)

dataset = models.Dataset(dir_name="26232224_SabatiniDM_Cell_2015", pmid="26232224", journal="Cell", year="2015", species="human",
                  initial_condition="t0", cell_line="Jurkat", type="ko", library="Addgene_1000000067",
                  norm_method="350_noness", treatment="", other_condition="", culture_days="", sample="normal", is_initial_condition=False,
                  source="counts", first_author="Birsoy K", last_author="Sabatini DM",
                  title="An Essential Role of the Mitochondrial Electron Transport Chain in Cell Proliferation Is to Enable Aspartate Synthesis", contact="Yingbo Cui", public_status="public")
db.session.add(dataset)

db.session.commit()


#dataset = models.Dataset(dir_name="24336569_LanderES_Science_2014, pmid=24336569", journal="Science", year="2014", species="human", initial_condition="HL60_initial,KBM7_initial", cell_line="HL60", type="ko", library="Addgene_51043-8", norm_method="none", treatment="", other_condition="", culture_days="", sample="HL60_initial", is_initial_condition=True, source="counts", first_author="Wang T", last_author="Lander ES", title="Genetic Screens in Human Cells Using the CRISPR-Cas9 System", contact="Yingbo Cui", public_status="public")

'''
Select with Flask-SQLAlchemy

cell=models.Dataset.query.filter_by(cell_line="KBM-7").all()
'''