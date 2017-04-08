from app import db, models

'''
dataset = models.Dataset(dir_name="24336569_LanderES_Science_2014", pmid="24336569", journal="Science", year="2014", organism="human",
                  initial_condition="HL60_initial,KBM7_initial", cell_line="HL60", type="ko", library="Addgene_51043-8",
                  norm_method="none", treatment="", other_condition="", culture_days="", sample="HL60_initial", is_initial_condition=True,
                  source="counts", first_author="Wang T", last_author="Lander ES",
                  title="Genetic Screens in Human Cells Using the CRISPR-Cas9 System", contact="Yingbo Cui", public_status="public")
db.session.add(dataset)

dataset = models.Dataset(dir_name="24336569_LanderES_Science_2014", pmid="24336569", journal="Science", year="2014", organism="human",
                  initial_condition="HL60_initial,KBM7_initial", cell_line="KBM-7", type="ko", library="Addgene_51043-8",
                  norm_method="none", treatment="", other_condition="", culture_days="", sample="KBM7_initial", is_initial_condition=True,
                  source="counts", first_author="Wang T", last_author="Lander ES",
                  title="Genetic Screens in Human Cells Using the CRISPR-Cas9 System", contact="Yingbo Cui", public_status="public")
db.session.add(dataset)
'''

dataset = models.Dataset(dir_name="24336569_LanderES_Science_2014", pmid="24336569", journal="Science", year="2014", organism="human",
                  initial_condition="HL60_initial,KBM7_initial", cell_line="HL60", type="ko", library="Addgene_51043-8",
                  norm_method="none", treatment="", other_condition="", culture_days="", sample="HL60_final", is_initial_condition=False,
                  source="counts", first_author="Wang T", last_author="Lander ES",
                  title="Genetic Screens in Human Cells Using the CRISPR-Cas9 System", contact="Yingbo Cui", public_status="public")
db.session.add(dataset)

dataset = models.Dataset(dir_name="24336569_LanderES_Science_2014", pmid="24336569", journal="Science", year="2014", organism="human",
                  initial_condition="HL60_initial,KBM7_initial", cell_line="KBM-7", type="ko", library="Addgene_51043-8",
                  norm_method="none", treatment="", other_condition="", culture_days="", sample="KBM7_final", is_initial_condition=False,
                  source="counts", first_author="Wang T", last_author="Lander ES",
                  title="Genetic Screens in Human Cells Using the CRISPR-Cas9 System", contact="Yingbo Cui", public_status="public")
db.session.add(dataset)

db.session.commit()


#dataset = models.Dataset(dir_name="24336569_LanderES_Science_2014, pmid=24336569", journal="Science", year="2014", organism="human", initial_condition="HL60_initial,KBM7_initial", cell_line="HL60", type="ko", library="Addgene_51043-8", norm_method="none", treatment="", other_condition="", culture_days="", sample="HL60_initial", is_initial_condition=True, source="counts", first_author="Wang T", last_author="Lander ES", title="Genetic Screens in Human Cells Using the CRISPR-Cas9 System", contact="Yingbo Cui", public_status="public")

'''
Select with Flask-SQLAlchemy

cell=models.Dataset.query.filter_by(cell_line="KBM-7").all()
'''