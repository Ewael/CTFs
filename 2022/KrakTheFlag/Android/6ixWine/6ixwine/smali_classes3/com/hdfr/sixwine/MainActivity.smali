.class public Lcom/hdfr/sixwine/MainActivity;
.super Landroidx/appcompat/app/AppCompatActivity;
.source "MainActivity.java"


# instance fields
.field private admin_secret:Ljava/lang/String;

.field btn_book:Landroid/widget/Button;

.field private rsv_txt:Landroid/widget/EditText;

.field private vip_link:Landroid/widget/TextView;


# direct methods
.method public constructor <init>()V
    .locals 1

    .line 19
    invoke-direct {p0}, Landroidx/appcompat/app/AppCompatActivity;-><init>()V

    .line 23
    const-string v0, ""

    iput-object v0, p0, Lcom/hdfr/sixwine/MainActivity;->admin_secret:Ljava/lang/String;

    return-void
.end method

.method static synthetic access$000(Lcom/hdfr/sixwine/MainActivity;)Landroid/widget/EditText;
    .locals 1
    .param p0, "x0"    # Lcom/hdfr/sixwine/MainActivity;

    .line 19
    iget-object v0, p0, Lcom/hdfr/sixwine/MainActivity;->rsv_txt:Landroid/widget/EditText;

    return-object v0
.end method


# virtual methods
.method protected onCreate(Landroid/os/Bundle;)V
    .locals 10
    .param p1, "savedInstanceState"    # Landroid/os/Bundle;

    .line 29
    const-string v0, "FAILED"

    invoke-super {p0, p1}, Landroidx/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    .line 30
    const v1, 0x7f0b001e

    invoke-virtual {p0, v1}, Lcom/hdfr/sixwine/MainActivity;->setContentView(I)V

    .line 31
    const v1, 0x7f0801da

    invoke-virtual {p0, v1}, Lcom/hdfr/sixwine/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/widget/TextView;

    iput-object v1, p0, Lcom/hdfr/sixwine/MainActivity;->vip_link:Landroid/widget/TextView;

    .line 32
    const v1, 0x7f080067

    invoke-virtual {p0, v1}, Lcom/hdfr/sixwine/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/widget/Button;

    iput-object v1, p0, Lcom/hdfr/sixwine/MainActivity;->btn_book:Landroid/widget/Button;

    .line 33
    const v1, 0x7f08005f

    invoke-virtual {p0, v1}, Lcom/hdfr/sixwine/MainActivity;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/widget/EditText;

    iput-object v1, p0, Lcom/hdfr/sixwine/MainActivity;->rsv_txt:Landroid/widget/EditText;

    .line 36
    invoke-virtual {p0}, Lcom/hdfr/sixwine/MainActivity;->getApplicationContext()Landroid/content/Context;

    move-result-object v1

    const-string v2, "prefs"

    const/4 v3, 0x0

    invoke-virtual {v1, v2, v3}, Landroid/content/Context;->getSharedPreferences(Ljava/lang/String;I)Landroid/content/SharedPreferences;

    move-result-object v1

    const-string v4, "secret"

    const-string v5, "nope"

    invoke-interface {v1, v4, v5}, Landroid/content/SharedPreferences;->getString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    .line 37
    .local v1, "secret":Ljava/lang/String;
    const/4 v6, 0x1

    new-array v6, v6, [I

    aput v3, v6, v3

    .line 39
    .local v6, "u_registered":[I
    :try_start_0
    invoke-virtual {p0}, Lcom/hdfr/sixwine/MainActivity;->getIntent()Landroid/content/Intent;

    move-result-object v7

    .line 40
    .local v7, "intent":Landroid/content/Intent;
    invoke-virtual {v7}, Landroid/content/Intent;->getExtras()Landroid/os/Bundle;

    move-result-object v8

    const-string v9, "Secret"

    invoke-virtual {v8, v9}, Landroid/os/Bundle;->getString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v8

    iput-object v8, p0, Lcom/hdfr/sixwine/MainActivity;->admin_secret:Ljava/lang/String;
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    .line 44
    .end local v7    # "intent":Landroid/content/Intent;
    goto :goto_0

    .line 41
    :catch_0
    move-exception v7

    .line 43
    .local v7, "e":Ljava/lang/Exception;
    invoke-virtual {v7}, Ljava/lang/Exception;->toString()Ljava/lang/String;

    move-result-object v8

    invoke-static {v0, v8}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    .line 45
    .end local v7    # "e":Ljava/lang/Exception;
    :goto_0
    iget-object v7, p0, Lcom/hdfr/sixwine/MainActivity;->admin_secret:Ljava/lang/String;

    invoke-virtual {p0}, Lcom/hdfr/sixwine/MainActivity;->getApplicationContext()Landroid/content/Context;

    move-result-object v8

    invoke-virtual {v8, v2, v3}, Landroid/content/Context;->getSharedPreferences(Ljava/lang/String;I)Landroid/content/SharedPreferences;

    move-result-object v2

    invoke-interface {v2, v4, v5}, Landroid/content/SharedPreferences;->getString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v7, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    const-string v3, "HDFR"

    if-eqz v2, :cond_0

    .line 46
    const-string v2, "Welcome to VIP Panel !"

    invoke-static {v3, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 47
    new-instance v2, Landroid/content/Intent;

    invoke-direct {v2}, Landroid/content/Intent;-><init>()V

    .line 48
    .local v2, "intent2":Landroid/content/Intent;
    const-string v3, "com.hdfr.sixwine"

    const-string v4, "com.hdfr.sixwine.VipPanel"

    invoke-virtual {v2, v3, v4}, Landroid/content/Intent;->setClassName(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    .line 51
    :try_start_1
    invoke-virtual {p0, v2}, Lcom/hdfr/sixwine/MainActivity;->startActivity(Landroid/content/Intent;)V
    :try_end_1
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_1

    .line 56
    goto :goto_1

    .line 53
    :catch_1
    move-exception v3

    .line 55
    .local v3, "e":Ljava/lang/Exception;
    invoke-virtual {v3}, Ljava/lang/Exception;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-static {v0, v4}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    .line 57
    .end local v2    # "intent2":Landroid/content/Intent;
    .end local v3    # "e":Ljava/lang/Exception;
    :goto_1
    goto :goto_2

    .line 60
    :cond_0
    const-string v0, "It may be a GOOD thing to check your permissions"

    invoke-static {v3, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 64
    :goto_2
    iget-object v0, p0, Lcom/hdfr/sixwine/MainActivity;->btn_book:Landroid/widget/Button;

    new-instance v2, Lcom/hdfr/sixwine/MainActivity$1;

    invoke-direct {v2, p0, v6}, Lcom/hdfr/sixwine/MainActivity$1;-><init>(Lcom/hdfr/sixwine/MainActivity;[I)V

    invoke-virtual {v0, v2}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    .line 86
    return-void
.end method
