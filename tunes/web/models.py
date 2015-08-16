from django.db import models
from django.contrib.auth.models import User


TUNEBOOK_TYPE_CHOICES = (
    ('personal', 'Personal tune book'),
    ('tunebook', 'Tune book'),
    ('teacher', 'Teacher'),
    ('setlist', 'Set list'),
    )

SETTING_KEY_CHOICES = [
    'C#', 'A#m', 'G#Mix', 'D#Dor', 'E#Phr', 'F#Lyd', 'B#Loc',
    'F#', 'D#m', 'C#Mix', 'G#Dor', 'A#Phr', 'BLyd', 'E#Loc',
    'B', 'G#m', 'F#Mix', 'C#Dor', 'D#Phr', 'ELyd', 'A#Loc',
    'E', 'C#m', 'BMix', 'F#Dor', 'G#Phr', 'ALyd', 'D#Loc',
    'A', 'F#m', 'EMix', 'BDor', 'C#Phr', 'DLyd', 'G#Loc',
    'D', 'Bm', 'AMix', 'EDor', 'F#Phr', 'GLyd', 'C#Loc',
    'G', 'Em', 'DMix', 'ADor', 'BPhr', 'CLyd', 'F#Loc',
    'C', 'Am', 'GMix', 'DDor', 'EPhr', 'FLyd', 'BLoc',
    'F', 'Dm', 'CMix', 'GDor', 'APhr', 'BbLyd', 'ELoc',
    'Bb', 'Gm', 'FMix', 'CDor', 'DPhr', 'EbLyd', 'ALoc',
    'Eb', 'Cm', 'BbMix', 'FDor', 'GPhr', 'AbLyd', 'DLoc',
    'Ab', 'Fm', 'EbMix', 'BbDor', 'CPhr', 'DbLyd', 'GLoc',
    'Db', 'Bbm', 'AbMix', 'EbDor', 'FPhr', 'GbLyd', 'CLoc',
    'Gb', 'Ebm', 'DbMix', 'AbDor', 'BbPhr', 'CbLyd', 'FLoc',
    'Cb', 'Abm', 'GbMix', 'DbDor', 'EbPhr', 'FbLyd', 'BbLoc',
    'none']

# Create your models here.
class Tune(models.Model):
    title = models.CharField(max_length=255)    # T
    origin = models.CharField(max_length=255)   # O
    composer = models.CharField(max_length=255) # C
    created_by = models.ForeignKey(User)
    type = models.CharField(max_length=30)

class Setting(models.Model):
    created_by = models.ForeignKey(User)
    tune = models.ForeignKey(Tune)
    created_at = models.DateTimeField()
    last_modified = models.DateTimeField()
    meter = models.CharField(max_length=255)    # M
    unit_note = models.CharField(max_length=10) # L
    tempo = models.CharField(max_length=10)     # Q
    key = models.CharField(max_length=10)       # K
    staves = models.TextField()
    
    def __str__(self):
        return self.get_abc()

    def get_abc(self):
        abc = "%abc-2.1\n"

        
        
        abc += staves + "\n"
        
        return abc

    def load_from_abc(self, abc_source):
        pass
    

class TuneComment(models.Model):
    author = models.ForeignKey(User)
    content = models.TextField()
    timestamp = models.DateTimeField()

class Recording(models.Model):
    created_by = models.ForeignKey(User)
    description = models.TextField()
    filesystem = models.FileField()

class RecordingAnnotation(models.Model):
    created_by = models.ForeignKey(User)
    recording = models.ForeignKey(Recording)
    tune = models.ForeignKey(Tune, null=True)
    offset = models.IntegerField()

class TuneRelation(models.Model):
    name = models.CharField(max_length=255)
    tune = models.ForeignKey(Tune)

class TuneBook(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User)
    public = models.BooleanField()
    tunes = models.ManyToManyField(Tune)
    type = models.CharField(max_length=32, choices=TUNEBOOK_TYPE_CHOICES)
