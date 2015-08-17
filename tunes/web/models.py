from django.db import models
from django.contrib.auth.models import User

#         _,--,            _
#    __,-'____| ___      /' |
#  /'   `\,--,/'   `\  /'   |
# (       )  (       )'
#  \_   _/'  `\_   _/   
#    """        """

TUNEBOOK_TYPE_CHOICES = (
    ('personal', 'Personal tune book'),
    ('tunebook', 'Tune book'),
    ('teacher', 'Teacher'),
    ('setlist', 'Set list'),
    )

SETTING_KEY_CHOICES = [
    ('C#', 'C#'), ('A#m','A#m'), ('G#Mix', 'G#Mix'), ('D#Dor','D#Dor',),
    ('E#Phr','E#Phr',), ('F#Lyd','F#Lyd',), ('B#Loc','B#Loc',),
    ('F#','F#',), ('D#m','D#m',), ('C#Mix','C#Mix',), ('G#Dor','G#Dor',),
    ('A#Phr','A#Phr',), ('BLyd','BLyd',), ('E#Loc','E#Loc',),
    ('B','B',), ('G#m','G#m',), ('F#Mix','F#Mix',), ('C#Dor','C#Dor',),
    ('D#Phr','D#Phr',), ('ELyd','ELyd',), ('A#Loc','A#Loc',),
    ('E','E',), ('C#m','C#m',), ('BMix','BMix',), ('F#Dor','F#Dor',),
    ('G#Phr','G#Phr',), ('ALyd','ALyd',), ('D#Loc','D#Loc',),
    ('A','A',), ('F#m','F#m',), ('EMix','EMix',), ('BDor','BDor',),
    ('C#Phr','C#Phr',), ('DLyd','DLyd',), ('G#Loc','G#Loc',),
    ('D','D',), ('Bm','Bm',), ('AMix','AMix',), ('EDor','EDor',),
    ('F#Phr','F#Phr',), ('GLyd','GLyd',), ('C#Loc','C#Loc',),
    ('G','G',), ('Em','Em',), ('DMix','DMix',), ('ADor','ADor',),
    ('BPhr','BPhr',), ('CLyd','CLyd',), ('F#Loc','F#Loc',),
    ('C','C',), ('Am','Am',), ('GMix','GMix',), ('DDor','DDor',),
    ('EPhr','EPhr',), ('FLyd','FLyd',), ('BLoc','BLoc',),
    ('F','F',), ('Dm','Dm',), ('CMix','CMix',), ('GDor','GDor',),
    ('APhr','APhr',), ('BbLyd','BbLyd',), ('ELoc','ELoc',),
    ('Bb','Bb',), ('Gm','Gm',), ('FMix','FMix',), ('CDor','CDor',),
    ('DPhr','DPhr',), ('EbLyd','EbLyd',), ('ALoc','ALoc',),
    ('Eb','Eb',), ('Cm','Cm',), ('BbMix','BbMix',), ('FDor','FDor',),
    ('GPhr','GPhr',), ('AbLyd','AbLyd',), ('DLoc','DLoc',),
    ('Ab','Ab',), ('Fm','Fm',), ('EbMix','EbMix',), ('BbDor','BbDor',),
    ('CPhr','CPhr',), ('DbLyd','DbLyd',), ('GLoc','GLoc',),
    ('Db','Db',), ('Bbm','Bbm',), ('AbMix','AbMix',), ('EbDor','EbDor',),
    ('FPhr','FPhr',), ('GbLyd','GbLyd',), ('CLoc','CLoc',),
    ('Gb','Gb',), ('Ebm','Ebm',), ('DbMix','DbMix',), ('AbDor','AbDor',),
    ('BbPhr','BbPhr',), ('CbLyd','CbLyd',), ('FLoc','FLoc',),
    ('Cb','Cb',), ('Abm','Abm',), ('GbMix','GbMix',), ('DbDor','DbDor',),
    ('EbPhr','EbPhr',), ('FbLyd','FbLyd',), ('BbLoc','BbLoc',), ('none', 'none')]

# Defines a type of tune, i.e. polska, polka, waltz, etc.
class TuneType(models.Model):
    # The name should be a translation field
    name = models.CharField(max_length=255)
    standard_tempo = models.CharField(max_length=10,
                                      null=True)
    standard_unit_note = models.CharField(max_length=10,
                                          null=True)

class Tune(models.Model):
    title = models.CharField(max_length=255)    # T
    origin = models.CharField(max_length=255,   # O
                              null=True)
    composer = models.CharField(max_length=255, # C
                                null=True)
    created_by = models.ForeignKey(User)
    notes = models.CharField(max_length=255,    # N
                             null=True)
    type = models.ForeignKey(TuneType)

class TuneAlias(models.Model):
    alias = models.CharField(max_length=255)
    tune = models.ForeignKey(Tune)

class Setting(models.Model):
    created_by = models.ForeignKey(User)
    tune = models.ForeignKey(Tune)
    meter = models.CharField(max_length=255,    # M
                             null=True)
    unit_note = models.CharField(max_length=10, # L
                                 null=True)
    tempo = models.CharField(max_length=255,    # Q
                             null=True)
    key = models.CharField(max_length=10,       # K
                           choices=SETTING_KEY_CHOICES)
    notes = models.CharField(max_length=255,    # N
                             null=True)
    staves = models.TextField()
    created_at = models.DateTimeField()
    last_modified = models.DateTimeField()
    
    def __str__(self):
        return self.get_abc()

    def get_abc(self):
        abc = "%abc-2.1\n"
        abc += "X: %d\n" % self.id
        abc += "T: %s\n" % self.tune.title

        if (self.tune.origin is not None):
            abc += "O: %s\n" % self.tune.origin
            
        if (self.tune.composer is not None):
            abc += "C: %s\n" % self.tune.composer

        if (self.meter is not None):
            abc += "M: %s\n" % self.meter

        if (self.unit_note is not None):
            abc += "L: %s\n" % self.unit_note

        if (self.tempo is not None):
            abc += "Q: %s\n" % self.tempo

        abc += "K: %s\n" % self.key

        if (self.tune.notes is not None):
            abc += "N: %s\n" % self.tune.notes

        if (self.notes is not None):
            abc += "N: %s\n" % self.notes
        
        abc += staves + "\n"
        
        return abc    

class TuneComment(models.Model):
    author = models.ForeignKey(User)
    content = models.TextField()
    timestamp = models.DateTimeField()

class Recording(models.Model):
    created_by = models.ForeignKey(User)
    description = models.TextField(null=True)
    filesystem = models.FileField()

class RecordingAnnotation(models.Model):
    created_by = models.ForeignKey(User)
    recording = models.ForeignKey(Recording)
    tune = models.ForeignKey(Tune, null=True)
    offset = models.IntegerField() # in seconds

# class TuneRelation(models.Model):
#     name = models.CharField(max_length=255)
#     tune = models.ForeignKey(Tune)

class TuneBook(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User)
    public = models.BooleanField()
    tunes = models.ManyToManyField(Tune)
    type = models.CharField(max_length=32,
                            choices=TUNEBOOK_TYPE_CHOICES)
