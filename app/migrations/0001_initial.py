# Generated by Django 4.2.11 on 2024-04-02 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('img', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='comentario_pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=500)),
                ('visibilidad', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='comentario_serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=500)),
                ('visibilidad', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sinopsis', models.TextField()),
                ('fecha_estreno', models.DateField()),
                ('img', models.CharField(max_length=300)),
                ('url_trailer', models.CharField(max_length=300)),
                ('director', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='plataforma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('img', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('sinopsis', models.TextField()),
                ('img', models.CharField(max_length=300)),
                ('trailer', models.CharField(max_length=300)),
                ('director', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('tipo', models.IntegerField()),
                ('img', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='valoracion_serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valoracion', models.IntegerField(null=True)),
                ('estado', models.IntegerField(null=True)),
                ('ultimo_capitulo', models.IntegerField(null=True)),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.serie')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='valoracion_pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valoracion', models.IntegerField(null=True)),
                ('estado', models.IntegerField(null=True)),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pelicula')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='temporada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('sinopsis', models.TextField()),
                ('img', models.CharField(max_length=300)),
                ('fecha_estreno', models.DateField()),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.serie')),
            ],
        ),
        migrations.CreateModel(
            name='series_favoritas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.serie')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='serie_genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.genero')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.serie')),
            ],
        ),
        migrations.CreateModel(
            name='respuestas_series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=500)),
                ('visibilidad', models.BooleanField(default=True)),
                ('comentario_series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.comentario_serie')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='respuestas_peliculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=500)),
                ('visibilidad', models.BooleanField(default=True)),
                ('comentario_peliculas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.comentario_pelicula')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='plataforma_serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plataforma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.plataforma')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.serie')),
            ],
        ),
        migrations.CreateModel(
            name='plataforma_pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pelicula')),
                ('plataforma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.plataforma')),
            ],
        ),
        migrations.CreateModel(
            name='peliculas_favoritas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pelicula')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='pelicula_genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.genero')),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pelicula')),
            ],
        ),
        migrations.CreateModel(
            name='foro_serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.serie')),
            ],
        ),
        migrations.CreateModel(
            name='foro_pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pelicula')),
            ],
        ),
        migrations.AddField(
            model_name='comentario_serie',
            name='foro_series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.foro_serie'),
        ),
        migrations.AddField(
            model_name='comentario_serie',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
        migrations.AddField(
            model_name='comentario_pelicula',
            name='foro_peliculas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.foro_pelicula'),
        ),
        migrations.AddField(
            model_name='comentario_pelicula',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
        migrations.CreateModel(
            name='capitulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('sinopsis', models.TextField()),
                ('img', models.CharField(max_length=300)),
                ('fecha_estreno', models.DateField()),
                ('temporada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.temporada')),
            ],
        ),
        migrations.CreateModel(
            name='actor_serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_actor', models.CharField(max_length=50)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.actor')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.serie')),
            ],
        ),
        migrations.CreateModel(
            name='actor_pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_actor', models.CharField(max_length=50)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.actor')),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pelicula')),
            ],
        ),
    ]
