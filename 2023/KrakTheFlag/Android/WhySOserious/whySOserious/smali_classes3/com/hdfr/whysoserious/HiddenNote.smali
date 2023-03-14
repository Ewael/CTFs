.class public Lcom/hdfr/whysoserious/HiddenNote;
.super Landroidx/appcompat/app/AppCompatActivity;
.source "HiddenNote.java"


# direct methods
.method public constructor <init>()V
    .locals 0

    .line 8
    invoke-direct {p0}, Landroidx/appcompat/app/AppCompatActivity;-><init>()V

    return-void
.end method


# virtual methods
.method protected onCreate(Landroid/os/Bundle;)V
    .locals 4
    .param p1, "savedInstanceState"    # Landroid/os/Bundle;

    .line 12
    invoke-super {p0, p1}, Landroidx/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    .line 13
    const v0, 0x7f0b001d

    invoke-virtual {p0, v0}, Lcom/hdfr/whysoserious/HiddenNote;->setContentView(I)V

    .line 14
    const-string v0, "Jryy qbar, abj gel sbhegl-frira"

    const-string v1, "HDFR"

    invoke-static {v1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 15
    const-string v0, "KE1heWJlIHNpeHR5LWZvdXIgYWxzbyA/KQ=="

    invoke-static {v1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 16
    invoke-virtual {p0}, Lcom/hdfr/whysoserious/HiddenNote;->getApplicationContext()Landroid/content/Context;

    move-result-object v0

    const-string v2, "prefs"

    const/4 v3, 0x0

    invoke-virtual {v0, v2, v3}, Landroid/content/Context;->getSharedPreferences(Ljava/lang/String;I)Landroid/content/SharedPreferences;

    move-result-object v0

    const-string v2, "secret_key"

    const-string v3, "nope"

    invoke-interface {v0, v2, v3}, Landroid/content/SharedPreferences;->getString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    invoke-static {v1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 17
    return-void
.end method
