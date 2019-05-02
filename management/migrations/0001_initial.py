
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contracting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('expire_date', models.DateField()),
                ('period', models.IntegerField(default=0)),
                ('deposit', models.DecimalField(decimal_places=3, max_digits=10)),
                ('dmg_deposit', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Dorm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dorm_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('floor', models.IntegerField(default=1)),
                ('elec_unit', models.DecimalField(decimal_places=3, max_digits=10)),
                ('water_unit', models.DecimalField(decimal_places=3, max_digits=10)),
                ('room_amount', models.IntegerField(default=1)),
                ('tel', models.CharField(default='0000000000', max_length=10, unique=True)),
                ('taxid', models.CharField(default='000-000', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('emp_phone', models.CharField(max_length=10, unique=True)),
                ('dorm_dorm_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.Dorm')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_desc', models.TextField()),
                ('price_per_unit', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.TextField()),
                ('line', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', models.DateField()),
                ('month_no', models.IntegerField(default=1)),
                ('rent_number', models.IntegerField(default=0)),
                ('total', models.DecimalField(decimal_places=3, max_digits=10)),
                ('status', models.CharField(choices=[('01', 'wait_pay'), ('02', 'wait_confirm')], default='01', max_length=2)),
                ('contracting_contract_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.Contracting')),
            ],
        ),
        migrations.CreateModel(
            name='Report_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10)),
                ('room_floor', models.IntegerField(default=1)),
                ('room_rate', models.DecimalField(decimal_places=3, max_digits=10)),
                ('status', models.CharField(choices=[('01', 'Available'), ('02', 'Full'), ('03', 'Booked')], default='01', max_length=2)),
                ('room_type', models.CharField(choices=[('01', 'Fan'), ('02', 'AirCondition')], default='01', max_length=2)),
                ('dorm_dorm_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.Dorm')),
            ],
        ),
        migrations.CreateModel(
            name='Reporting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_desc', models.TextField()),
                ('report_date', models.DateTimeField()),
                ('report_type_type_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.Report_type')),
                ('room_room_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.Room')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('payment_datetime', models.DateTimeField()),
                ('bill_picture', models.ImageField(blank=True, null=True, upload_to='payments_%Y-%m-%D')),
                ('payment_confirm', models.CharField(choices=[('01', 'Unpaid'), ('02', 'Paid')], default='01', max_length=2)),
                ('invoice_invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.Invoice')),
            ],
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname_guest', models.CharField(max_length=255)),
                ('lname_guest', models.CharField(max_length=255)),
                ('arrive_date', models.DateTimeField()),
                ('post_type', models.CharField(max_length=255)),
                ('packaging', models.CharField(max_length=255)),
                ('track_number', models.CharField(max_length=13, unique=True)),
                ('guest_guest_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.Guest')),
            ],
        ),
        migrations.CreateModel(
            name='Logging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_date', models.DateTimeField()),
                ('employee_emp_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('total', models.DecimalField(decimal_places=3, max_digits=10)),
                ('unit', models.DecimalField(decimal_places=3, max_digits=10)),
                ('expense_exp_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.Expense')),
                ('invoice_invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.Invoice')),
            ],
        ),
        migrations.AddField(
            model_name='contracting',
            name='guest_guest_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.Guest'),
        ),
        migrations.AddField(
            model_name='contracting',
            name='room_room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='management.Room'),
        ),
    ]
