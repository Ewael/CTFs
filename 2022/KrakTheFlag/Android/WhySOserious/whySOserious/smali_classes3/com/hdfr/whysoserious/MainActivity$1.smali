.class Lcom/hdfr/whysoserious/MainActivity$1;
.super Ljava/lang/Object;
.source "MainActivity.java"

# interfaces
.implements Landroid/view/View$OnClickListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/hdfr/whysoserious/MainActivity;->onCreate(Landroid/os/Bundle;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/hdfr/whysoserious/MainActivity;


# direct methods
.method constructor <init>(Lcom/hdfr/whysoserious/MainActivity;)V
    .locals 0
    .param p1, "this$0"    # Lcom/hdfr/whysoserious/MainActivity;

    .line 67
    iput-object p1, p0, Lcom/hdfr/whysoserious/MainActivity$1;->this$0:Lcom/hdfr/whysoserious/MainActivity;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 4
    .param p1, "view"    # Landroid/view/View;

    .line 71
    iget-object v0, p0, Lcom/hdfr/whysoserious/MainActivity$1;->this$0:Lcom/hdfr/whysoserious/MainActivity;

    iget-object v0, v0, Lcom/hdfr/whysoserious/MainActivity;->Code_Input:Landroid/widget/EditText;

    invoke-virtual {v0}, Landroid/widget/EditText;->getText()Landroid/text/Editable;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v0

    .line 72
    .local v0, "code":Ljava/lang/String;
    iget-object v1, p0, Lcom/hdfr/whysoserious/MainActivity$1;->this$0:Lcom/hdfr/whysoserious/MainActivity;

    invoke-virtual {v1, v0}, Lcom/hdfr/whysoserious/MainActivity;->magic(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    const-string v2, "zFKDWInq"

    invoke-virtual {v1, v2}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    const/4 v2, 0x1

    if-eqz v1, :cond_0

    .line 74
    iget-object v1, p0, Lcom/hdfr/whysoserious/MainActivity$1;->this$0:Lcom/hdfr/whysoserious/MainActivity;

    invoke-virtual {v1}, Lcom/hdfr/whysoserious/MainActivity;->getApplicationContext()Landroid/content/Context;

    move-result-object v1

    const-string v3, "You found the valid code ! well one"

    invoke-static {v1, v3, v2}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object v1

    invoke-virtual {v1}, Landroid/widget/Toast;->show()V

    goto :goto_0

    .line 78
    :cond_0
    iget-object v1, p0, Lcom/hdfr/whysoserious/MainActivity$1;->this$0:Lcom/hdfr/whysoserious/MainActivity;

    iget v3, v1, Lcom/hdfr/whysoserious/MainActivity;->Attempts_left:I

    sub-int/2addr v3, v2

    iput v3, v1, Lcom/hdfr/whysoserious/MainActivity;->Attempts_left:I

    .line 79
    iget-object v1, p0, Lcom/hdfr/whysoserious/MainActivity$1;->this$0:Lcom/hdfr/whysoserious/MainActivity;

    iget-object v1, v1, Lcom/hdfr/whysoserious/MainActivity;->AttemptsText:Landroid/widget/TextView;

    iget-object v2, p0, Lcom/hdfr/whysoserious/MainActivity$1;->this$0:Lcom/hdfr/whysoserious/MainActivity;

    iget v2, v2, Lcom/hdfr/whysoserious/MainActivity;->Attempts_left:I

    invoke-static {v2}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    .line 80
    iget-object v1, p0, Lcom/hdfr/whysoserious/MainActivity$1;->this$0:Lcom/hdfr/whysoserious/MainActivity;

    iget v1, v1, Lcom/hdfr/whysoserious/MainActivity;->Attempts_left:I

    if-nez v1, :cond_1

    .line 82
    iget-object v1, p0, Lcom/hdfr/whysoserious/MainActivity$1;->this$0:Lcom/hdfr/whysoserious/MainActivity;

    const v2, 0x7f0b0030

    invoke-virtual {v1, v2}, Lcom/hdfr/whysoserious/MainActivity;->setContentView(I)V

    goto :goto_0

    .line 86
    :cond_1
    iget-object v1, p0, Lcom/hdfr/whysoserious/MainActivity$1;->this$0:Lcom/hdfr/whysoserious/MainActivity;

    const-string v2, "TICCC TACCCC"

    const/4 v3, 0x0

    invoke-static {v1, v2, v3}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object v1

    invoke-virtual {v1}, Landroid/widget/Toast;->show()V

    .line 89
    :goto_0
    return-void
.end method
