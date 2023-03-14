.class Lcom/hdfr/sixwine/MainActivity$1;
.super Ljava/lang/Object;
.source "MainActivity.java"

# interfaces
.implements Landroid/view/View$OnClickListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/hdfr/sixwine/MainActivity;->onCreate(Landroid/os/Bundle;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/hdfr/sixwine/MainActivity;

.field final synthetic val$u_registered:[I


# direct methods
.method constructor <init>(Lcom/hdfr/sixwine/MainActivity;[I)V
    .locals 0
    .param p1, "this$0"    # Lcom/hdfr/sixwine/MainActivity;

    .line 64
    iput-object p1, p0, Lcom/hdfr/sixwine/MainActivity$1;->this$0:Lcom/hdfr/sixwine/MainActivity;

    iput-object p2, p0, Lcom/hdfr/sixwine/MainActivity$1;->val$u_registered:[I

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 5
    .param p1, "view"    # Landroid/view/View;

    .line 67
    const-string v0, "WOW"

    const-string v1, "DGB"

    invoke-static {v1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 69
    iget-object v0, p0, Lcom/hdfr/sixwine/MainActivity$1;->this$0:Lcom/hdfr/sixwine/MainActivity;

    invoke-static {v0}, Lcom/hdfr/sixwine/MainActivity;->access$000(Lcom/hdfr/sixwine/MainActivity;)Landroid/widget/EditText;

    move-result-object v0

    invoke-virtual {v0}, Landroid/widget/EditText;->getText()Landroid/text/Editable;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v0

    .line 70
    .local v0, "name":Ljava/lang/String;
    invoke-virtual {v0}, Ljava/lang/String;->isEmpty()Z

    move-result v2

    const/4 v3, 0x0

    if-nez v2, :cond_0

    iget-object v2, p0, Lcom/hdfr/sixwine/MainActivity$1;->val$u_registered:[I

    aget v2, v2, v3

    if-nez v2, :cond_0

    .line 71
    const-string v2, "SHEESH"

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 72
    iget-object v1, p0, Lcom/hdfr/sixwine/MainActivity$1;->this$0:Lcom/hdfr/sixwine/MainActivity;

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "Thank you "

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v4, ", Your tickets will receive your tickets soon"

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2, v3}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object v1

    invoke-virtual {v1}, Landroid/widget/Toast;->show()V

    .line 73
    iget-object v1, p0, Lcom/hdfr/sixwine/MainActivity$1;->val$u_registered:[I

    const/4 v2, 0x1

    aput v2, v1, v3

    goto :goto_0

    .line 75
    :cond_0
    iget-object v2, p0, Lcom/hdfr/sixwine/MainActivity$1;->val$u_registered:[I

    aget v2, v2, v3

    if-eqz v2, :cond_1

    .line 77
    const-string v2, "DAMN"

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    .line 78
    iget-object v1, p0, Lcom/hdfr/sixwine/MainActivity$1;->this$0:Lcom/hdfr/sixwine/MainActivity;

    const-string v2, "I know 6ixWine is the greatest, but you already purchased a ticket !"

    invoke-static {v1, v2, v3}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object v1

    invoke-virtual {v1}, Landroid/widget/Toast;->show()V

    goto :goto_0

    .line 82
    :cond_1
    iget-object v1, p0, Lcom/hdfr/sixwine/MainActivity$1;->this$0:Lcom/hdfr/sixwine/MainActivity;

    const-string v2, "Please enter your name"

    invoke-static {v1, v2, v3}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object v1

    invoke-virtual {v1}, Landroid/widget/Toast;->show()V

    .line 84
    :goto_0
    return-void
.end method
