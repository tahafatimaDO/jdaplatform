# Generated by Django 3.1.6 on 2022-03-10 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jdaanalyticsapp', '0030_auto_20220308_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='securitymodel',
            name='issue',
            field=models.CharField(blank=True, choices=[('', 'Issue'), ('Afghanistan', 'Afghanistan'), ('Åland Islands', 'Åland Islands'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('American Samoa', 'American Samoa'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antarctica', 'Antarctica'), ('Antigua and Barbuda', 'Antigua and Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Aruba', 'Aruba'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bonaire, Sint Eustatius and Saba', 'Bonaire, Sint Eustatius and Saba'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Botswana', 'Botswana'), ('Bouvet Island', 'Bouvet Island'), ('Brazil', 'Brazil'), ('British Indian Ocean Territory', 'British Indian Ocean Territory'), ('Brunei', 'Brunei'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cabo Verde', 'Cabo Verde'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Cayman Islands', 'Cayman Islands'), ('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'), ('Chile', 'Chile'), ('China', 'China'), ('Christmas Island', 'Christmas Island'), ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'), ('Congo (the Democratic Republic of the)', 'Congo (the Democratic Republic of the)'), ('Cook Islands', 'Cook Islands'), ('Costa Rica', 'Costa Rica'), ("Côte d'Ivoire", "Côte d'Ivoire"), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Curaçao', 'Curaçao'), ('Cyprus', 'Cyprus'), ('Czechia', 'Czechia'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Eswatini', 'Eswatini'), ('Ethiopia', 'Ethiopia'), ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'), ('Faroe Islands', 'Faroe Islands'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('French Guiana', 'French Guiana'), ('French Polynesia', 'French Polynesia'), ('French Southern Territories', 'French Southern Territories'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Greece', 'Greece'), ('Greenland', 'Greenland'), ('Grenada', 'Grenada'), ('Guadeloupe', 'Guadeloupe'), ('Guam', 'Guam'), ('Guatemala', 'Guatemala'), ('Guernsey', 'Guernsey'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Heard Island and McDonald Islands', 'Heard Island and McDonald Islands'), ('Holy See', 'Holy See'), ('Honduras', 'Honduras'), ('Hong Kong', 'Hong Kong'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Isle of Man', 'Isle of Man'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jersey', 'Jersey'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kiribati', 'Kiribati'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Macao', 'Macao'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Marshall Islands', 'Marshall Islands'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mayotte', 'Mayotte'), ('Mexico', 'Mexico'), ('Micronesia (Federated States of)', 'Micronesia (Federated States of)'), ('Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Montserrat', 'Montserrat'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar', 'Myanmar'), ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Caledonia', 'New Caledonia'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Niue', 'Niue'), ('Norfolk Island', 'Norfolk Island'), ('North Korea', 'North Korea'), ('North Macedonia', 'North Macedonia'), ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palau', 'Palau'), ('Palestine, State of', 'Palestine, State of'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Pitcairn', 'Pitcairn'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Réunion', 'Réunion'), ('Romania', 'Romania'), ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('Saint Barthélemy', 'Saint Barthélemy'), ('Saint Helena, Ascension and Tristan da Cunha', 'Saint Helena, Ascension and Tristan da Cunha'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Saint Lucia', 'Saint Lucia'), ('Saint Martin (French part)', 'Saint Martin (French part)'), ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'), ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'), ('Samoa', 'Samoa'), ('San Marino', 'San Marino'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Sint Maarten (Dutch part)', 'Sint Maarten (Dutch part)'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('South Georgia and the South Sandwich Islands', 'South Georgia and the South Sandwich Islands'), ('South Korea', 'South Korea'), ('South Sudan', 'South Sudan'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Svalbard and Jan Mayen', 'Svalbard and Jan Mayen'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Taiwan', 'Taiwan'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Timor-Leste', 'Timor-Leste'), ('Togo', 'Togo'), ('Tokelau', 'Tokelau'), ('Tonga', 'Tonga'), ('Trinidad and Tobago', 'Trinidad and Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Turks and Caicos Islands', 'Turks and Caicos Islands'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'), ('United States Minor Outlying Islands', 'United States Minor Outlying Islands'), ('United States of America', 'United States of America'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vanuatu', 'Vanuatu'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Virgin Islands (British)', 'Virgin Islands (British)'), ('Virgin Islands (U.S.)', 'Virgin Islands (U.S.)'), ('Wallis and Futuna', 'Wallis and Futuna'), ('Western Sahara', 'Western Sahara'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe'), ('Teset Comp', 'Teset Comp'), ('Teset Comp 5', 'Teset Comp 5'), ('Teset Comp 6', 'Teset Comp 6'), ('Teset Comp12', 'Teset Comp12'), ('Teset Comp2', 'Teset Comp2'), ('Teset Comp3', 'Teset Comp3'), ('Teset Comp4', 'Teset Comp4')], max_length=200, null=True),
        ),
    ]
