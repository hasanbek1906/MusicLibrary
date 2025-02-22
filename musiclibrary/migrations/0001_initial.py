# Generated by Django 4.2.7 on 2023-11-27 20:46

from django.db import migrations, models
import django.db.models.deletion
import musiclibrary.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cover', models.ImageField(max_length=500, upload_to=musiclibrary.models.AlbumModel.path_album_cover)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'album',
                'verbose_name_plural': 'albums',
                'db_table': 'albums',
                'ordering': ['-uploaded_at'],
            },
        ),
        migrations.CreateModel(
            name='ArtistModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, help_text='Your artist name that will be attached to your content.If not passed, full name will be considered instead.', max_length=20)),
            ],
            options={
                'verbose_name': 'artist',
                'verbose_name_plural': 'artists',
                'db_table': 'artists',
            },
        ),
        migrations.CreateModel(
            name='FollowModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'following',
                'verbose_name_plural': 'followings',
                'db_table': 'followings',
            },
        ),
        migrations.CreateModel(
            name='SongModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('lyrics', models.TextField(blank=True, null=True)),
                ('cover', models.ImageField(max_length=500, upload_to=musiclibrary.models.SongModel.path_song_cover)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('file', models.FileField(max_length=5000, upload_to=musiclibrary.models.SongModel.path_song_file)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='songs_in_album', to='musiclibrary.albummodel')),
                ('artists', models.ManyToManyField(related_name='songs_by_artist', to='musiclibrary.artistmodel')),
            ],
            options={
                'verbose_name': 'song',
                'verbose_name_plural': 'songs',
                'db_table': 'songs',
                'ordering': ['-uploaded_at'],
            },
        ),
        migrations.CreateModel(
            name='LikedContentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albums', models.ManyToManyField(blank=True, related_name='liked_albums', to='musiclibrary.albummodel')),
                ('songs', models.ManyToManyField(blank=True, related_name='liked_songs', to='musiclibrary.songmodel')),
            ],
            options={
                'verbose_name': 'liked content',
                'verbose_name_plural': 'liked contents',
                'db_table': 'liked_content',
            },
        ),
    ]
