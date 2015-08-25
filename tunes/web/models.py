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

SETTING_KEY_CHOICES = [('A', 'A major'), ('A#Loc', 'A# locrian'), ('A#Phr', 'A# phrygian'), ('A#m', 'A# minor'), ('ADor', 'A dorian'), ('ALoc', 'A locrian'), ('ALyd', 'A lydian'), ('AMix', 'A mixolydian'), ('APhr', 'A phrygian'), ('Ab', 'Ab major'), ('AbDor', 'Ab dorian'), ('AbLyd', 'Ab lydian'), ('AbMix', 'Ab mixolydian'), ('Abm', 'Ab minor'), ('Am', 'A minor'), ('B', 'B major'), ('B#Loc', 'B# locrian'), ('BDor', 'B dorian'), ('BLoc', 'B locrian'), ('BLyd', 'B lydian'), ('BMix', 'B mixolydian'), ('BPhr', 'B phrygian'), ('Bb', 'Bb major'), ('BbDor', 'Bb dorian'), ('BbLoc', 'Bb locrian'), ('BbLyd', 'Bb lydian'), ('BbMix', 'Bb mixolydian'), ('BbPhr', 'Bb phrygian'), ('Bbm', 'Bb minor'), ('Bm', 'B minor'), ('C', 'C major'), ('C#', 'C# major'), ('C#Dor', 'C# dorian'), ('C#Loc', 'C# locrian'), ('C#Mix', 'C# mixolydian'), ('C#Phr', 'C# phrygian'), ('C#m', 'C# minor'), ('CDor', 'C dorian'), ('CLoc', 'C locrian'), ('CLyd', 'C lydian'), ('CMix', 'C mixolydian'), ('CPhr', 'C phrygian'), ('Cb', 'Cb major'), ('CbLyd', 'Cb lydian'), ('Cm', 'C minor'), ('D', 'D major'), ('D#Dor', 'D# dorian'), ('D#Loc', 'D# locrian'), ('D#Phr', 'D# phrygian'), ('D#m', 'D# minor'), ('DDor', 'D dorian'), ('DLoc', 'D locrian'), ('DLyd', 'D lydian'), ('DMix', 'D mixolydian'), ('DPhr', 'D phrygian'), ('Db', 'Db major'), ('DbDor', 'Db dorian'), ('DbLyd', 'Db lydian'), ('DbMix', 'Db mixolydian'), ('Dm', 'D minor'), ('E', 'E major'), ('E#Loc', 'E# locrian'), ('E#Phr', 'E# phrygian'), ('EDor', 'E dorian'), ('ELoc', 'E locrian'), ('ELyd', 'E lydian'), ('EMix', 'E mixolydian'), ('EPhr', 'E phrygian'), ('Eb', 'Eb major'), ('EbDor', 'Eb dorian'), ('EbLyd', 'Eb lydian'), ('EbMix', 'Eb mixolydian'), ('EbPhr', 'Eb phrygian'), ('Ebm', 'Eb minor'), ('Em', 'E minor'), ('F', 'F major'), ('F#', 'F# major'), ('F#Dor', 'F# dorian'), ('F#Loc', 'F# locrian'), ('F#Lyd', 'F# lydian'), ('F#Mix', 'F# mixolydian'), ('F#Phr', 'F# phrygian'), ('F#m', 'F# minor'), ('FDor', 'F dorian'), ('FLoc', 'F locrian'), ('FLyd', 'F lydian'), ('FMix', 'F mixolydian'), ('FPhr', 'F phrygian'), ('FbLyd', 'Fb lydian'), ('Fm', 'F minor'), ('G', 'G major'), ('G#Dor', 'G# dorian'), ('G#Loc', 'G# locrian'), ('G#Mix', 'G# mixolydian'), ('G#Phr', 'G# phrygian'), ('G#m', 'G# minor'), ('GDor', 'G dorian'), ('GLoc', 'G locrian'), ('GLyd', 'G lydian'), ('GMix', 'G mixolydian'), ('GPhr', 'G phrygian'), ('Gb', 'Gb major'), ('GbLyd', 'Gb lydian'), ('GbMix', 'Gb mixolydian'), ('Gm', 'G minor'), ('none', 'none')]

class TunesUser(models.Model):
    user = models.OneToOneField(User)
    description = models.TextField(null=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)

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
    source = models.CharField(max_length=255,   # S
                              null=True)
    created_by = models.ForeignKey(TunesUser)
    notes = models.CharField(max_length=255,    # N
                             null=True)
    type = models.ForeignKey(TuneType)

class TuneAlias(models.Model):
    alias = models.CharField(max_length=255)
    tune = models.ForeignKey(Tune)

class Setting(models.Model):
    created_by = models.ForeignKey(TunesUser)
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
        abc += "R: %s\n" % self.tune.type.name
        
        if (self.tune.origin is not None):
            abc += "O: %s\n" % self.tune.origin

        if (self.tune.source is not None):
            abc += "S: %s\n" % self.tune.source
            
        if (self.tune.composer is not None):
            abc += "C: %s\n" % self.tune.composer

        if (self.meter is not None):
            abc += "M: %s\n" % self.meter

        if (self.unit_note is not None):
            abc += "L: %s\n" % self.unit_note

        if (self.tempo is not None):
            abc += "Q: %s\n" % self.tempo

        if (self.tune.notes is not None):
            abc += "N: %s\n" % self.tune.notes

        if (self.notes is not None):
            abc += "N: %s\n" % self.notes
        
        abc += "K: %s\n" % self.key

        abc += staves + "\n"
        
        return abc    

class TuneComment(models.Model):
    author = models.ForeignKey(TunesUser)
    content = models.TextField()
    timestamp = models.DateTimeField()

class Recording(models.Model):
    created_by = models.ForeignKey(TunesUser)
    description = models.TextField(null=True)
    filesystem = models.FileField()

class RecordingAnnotation(models.Model):
    created_by = models.ForeignKey(TunesUser)
    recording = models.ForeignKey(Recording)
    tune = models.ForeignKey(Tune, null=True)
    offset = models.IntegerField() # in seconds

# class TuneRelation(models.Model):
#     name = models.CharField(max_length=255)
#     tune = models.ForeignKey(Tune)

class TuneBook(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(TunesUser)
    public = models.BooleanField()
    tunes = models.ManyToManyField(Tune)
    type = models.CharField(max_length=32,
                            choices=TUNEBOOK_TYPE_CHOICES)
