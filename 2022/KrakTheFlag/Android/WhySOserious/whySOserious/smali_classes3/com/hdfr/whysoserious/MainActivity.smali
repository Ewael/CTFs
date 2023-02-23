.class public Lcom/hdfr/whysoserious/MainActivity;
.super Landroidx/appcompat/app/AppCompatActivity;
.source "MainActivity.java"


# instance fields
.field AttemptsText:Landroid/widget/TextView;

.field Attempts_left:I

.field Code_Input:Landroid/widget/EditText;

.field Defuse:Landroid/widget/Button;

.field def_code:Ljava/lang/String;


# direct methods
.method static constructor <clinit>()V
    .locals 1

    .line 28
    const-string v0, "defuse"

    invoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V

    .line 29
    return-void
.end method

.method public constructor <init>()V
    .locals 0

    .line 17
    invoke-direct {p0}, Landroidx/appcompat/app/AppCompatActivity;-><init>()V

    return-void
.end method


# virtual methods
.method public native magic(Ljava/lang/String;)Ljava/lang/String;
.end method

.method protected onCreate(Landroid/os/Bundle;)V
    .locals 5
    .param p1, "savedInstanceState"    # Landroid/os/Bundle;

    .line 33
    const-string v0, "FAILED"

    invoke-super {p0, p1}, Landroidx/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    .line 34
    const v1, 0x7f0b001f

    invoke-virtual {p0, v1}, Lcom/hdfr/whysoserious/MainActivity;->setContentView(I)V

    .line 36
    const v1, 0x7f080156

    invoke-virtual {p0, v1}, Lcom/hdfr/whysoserious/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/widget/EditText;

    iput-object v1, p0, Lcom/hdfr/whysoserious/MainActivity;->Code_Input:Landroid/widget/EditText;

    .line 37
    const v1, 0x7f080065

    invoke-virtual {p0, v1}, Lcom/hdfr/whysoserious/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/widget/Button;

    iput-object v1, p0, Lcom/hdfr/whysoserious/MainActivity;->Defuse:Landroid/widget/Button;

    .line 38
    const/4 v1, 0x3

    iput v1, p0, Lcom/hdfr/whysoserious/MainActivity;->Attempts_left:I

    .line 39
    const v1, 0x7f080001

    invoke-virtual {p0, v1}, Lcom/hdfr/whysoserious/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/widget/TextView;

    iput-object v1, p0, Lcom/hdfr/whysoserious/MainActivity;->AttemptsText:Landroid/widget/TextView;

    .line 40
    iget v2, p0, Lcom/hdfr/whysoserious/MainActivity;->Attempts_left:I

    invoke-static {v2}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    .line 43
    :try_start_0
    invoke-virtual {p0}, Lcom/hdfr/whysoserious/MainActivity;->getIntent()Landroid/content/Intent;

    move-result-object v1

    .line 44
    .local v1, "intent":Landroid/content/Intent;
    invoke-virtual {v1}, Landroid/content/Intent;->getExtras()Landroid/os/Bundle;

    move-result-object v2

    const-string v3, "DefCode"

    invoke-virtual {v2, v3}, Landroid/os/Bundle;->getString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v2

    iput-object v2, p0, Lcom/hdfr/whysoserious/MainActivity;->def_code:Ljava/lang/String;
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    .line 48
    .end local v1    # "intent":Landroid/content/Intent;
    goto :goto_0

    .line 45
    :catch_0
    move-exception v1

    .line 47
    .local v1, "e":Ljava/lang/Exception;
    invoke-virtual {v1}, Ljava/lang/Exception;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v2}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    .line 49
    .end local v1    # "e":Ljava/lang/Exception;
    :goto_0
    iget-object v1, p0, Lcom/hdfr/whysoserious/MainActivity;->def_code:Ljava/lang/String;

    invoke-virtual {p0}, Lcom/hdfr/whysoserious/MainActivity;->getApplicationContext()Landroid/content/Context;

    move-result-object v2

    const-string v3, "prefs"

    const/4 v4, 0x0

    invoke-virtual {v2, v3, v4}, Landroid/content/Context;->getSharedPreferences(Ljava/lang/String;I)Landroid/content/SharedPreferences;

    move-result-object v2

    const-string v3, "def_code"

    const-string v4, "no"

    invoke-interface {v2, v3, v4}, Landroid/content/SharedPreferences;->getString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    const-string v2, "HDFR"

    if-eqz v1, :cond_0

    .line 50
    const-string v1, "Wow !! It was a close call ! Now let\'s free Alfred and Robin before it\'s too late!"

    invoke-static {v2, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 51
    new-instance v1, Landroid/content/Intent;

    invoke-direct {v1}, Landroid/content/Intent;-><init>()V

    .line 52
    .local v1, "intent2":Landroid/content/Intent;
    const-string v2, "com.hdfr.whysoserious"

    const-string v3, "com.hdfr.whysoserious.Defuse"

    invoke-virtual {v1, v2, v3}, Landroid/content/Intent;->setClassName(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    .line 55
    :try_start_1
    invoke-virtual {p0, v1}, Lcom/hdfr/whysoserious/MainActivity;->startActivity(Landroid/content/Intent;)V
    :try_end_1
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_1

    .line 60
    goto :goto_1

    .line 57
    :catch_1
    move-exception v2

    .line 59
    .local v2, "e":Ljava/lang/Exception;
    invoke-virtual {v2}, Ljava/lang/Exception;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v0, v3}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    .line 61
    .end local v1    # "intent2":Landroid/content/Intent;
    .end local v2    # "e":Ljava/lang/Exception;
    :goto_1
    goto :goto_2

    .line 64
    :cond_0
    const-string v0, "Wrong Code HA HA HA HA HA"

    invoke-static {v2, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 67
    :goto_2
    iget-object v0, p0, Lcom/hdfr/whysoserious/MainActivity;->Defuse:Landroid/widget/Button;

    new-instance v1, Lcom/hdfr/whysoserious/MainActivity$1;

    invoke-direct {v1, p0}, Lcom/hdfr/whysoserious/MainActivity$1;-><init>(Lcom/hdfr/whysoserious/MainActivity;)V

    invoke-virtual {v0, v1}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    .line 91
    return-void
.end method
