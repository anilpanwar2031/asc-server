# Generated by Django 3.2.12 on 2022-11-10 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_alter_customuser_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GS1_Company_Prefix', models.CharField(blank=True, max_length=255)),
                ('GTIN', models.CharField(blank=True, max_length=255)),
                ('GTIN_8', models.CharField(blank=True, max_length=255)),
                ('GTIN_12_UPC', models.CharField(blank=True, max_length=255)),
                ('GTIN_13_EAN', models.CharField(blank=True, max_length=255)),
                ('Brand_Name', models.CharField(blank=True, max_length=255)),
                ('Brand_1_Language', models.CharField(blank=True, max_length=255)),
                ('Product_Description', models.CharField(blank=True, max_length=255)),
                ('Desc_1_Language', models.CharField(blank=True, max_length=255)),
                ('Product_Industry', models.CharField(blank=True, max_length=255)),
                ('Packaging_Level', models.CharField(blank=True, max_length=255)),
                ('Is_Variable', models.CharField(blank=True, max_length=255)),
                ('Is_Purchasable', models.CharField(blank=True, max_length=255)),
                ('Status_Label', models.CharField(blank=True, max_length=255)),
                ('Height', models.CharField(blank=True, max_length=255)),
                ('Width', models.CharField(blank=True, max_length=255)),
                ('Depth', models.CharField(blank=True, max_length=255)),
                ('Dimension_Measure', models.CharField(blank=True, max_length=255)),
                ('Gross_Weight', models.CharField(blank=True, max_length=255)),
                ('Net_Weight', models.CharField(blank=True, max_length=255)),
                ('Weight_Measure', models.CharField(blank=True, max_length=255)),
                ('SKU', models.CharField(blank=True, max_length=255)),
                ('Sub_brand_Name', models.CharField(blank=True, max_length=255)),
                ('Product_Description_Short', models.CharField(blank=True, max_length=255)),
                ('Label_Description', models.CharField(blank=True, max_length=255)),
                ('Net_Content_1_Count', models.CharField(blank=True, max_length=255)),
                ('Net_Content_1_Unit_of_Measure', models.CharField(blank=True, max_length=255)),
                ('Net_Content_2_Count', models.CharField(blank=True, max_length=255)),
                ('Net_Content_2_Unit_of_Measure', models.CharField(blank=True, max_length=255)),
                ('Net_Content_3_Count', models.CharField(blank=True, max_length=255)),
                ('Net_Content_3_Unit_of_Measure', models.CharField(blank=True, max_length=255)),
                ('Brand_Name_2', models.CharField(blank=True, max_length=255)),
                ('Brand_2_Language', models.CharField(blank=True, max_length=255)),
                ('Description_2', models.CharField(blank=True, max_length=255)),
                ('Desc_2_Language', models.CharField(blank=True, max_length=255)),
                ('Global_Product_Classification', models.CharField(blank=True, max_length=255)),
                ('Image_URL', models.FileField(null=True, upload_to='media/uploads/')),
                ('Image_URL_Validation', models.CharField(blank=True, max_length=255)),
                ('Target_Markets', models.CharField(blank=True, max_length=255)),
                ('Last_Modified_Date', models.DateField()),
            ],
        ),
    ]
