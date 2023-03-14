.class Lcom/hdfr/whysoserious/ExplodeFragment$1;
.super Ljava/lang/Object;
.source "ExplodeFragment.java"

# interfaces
.implements Landroid/view/View$OnClickListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/hdfr/whysoserious/ExplodeFragment;->onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/hdfr/whysoserious/ExplodeFragment;


# direct methods
.method constructor <init>(Lcom/hdfr/whysoserious/ExplodeFragment;)V
    .locals 0
    .param p1, "this$0"    # Lcom/hdfr/whysoserious/ExplodeFragment;

    .line 35
    iput-object p1, p0, Lcom/hdfr/whysoserious/ExplodeFragment$1;->this$0:Lcom/hdfr/whysoserious/ExplodeFragment;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 1
    .param p1, "view"    # Landroid/view/View;

    .line 38
    iget-object v0, p0, Lcom/hdfr/whysoserious/ExplodeFragment$1;->this$0:Lcom/hdfr/whysoserious/ExplodeFragment;

    invoke-virtual {v0}, Lcom/hdfr/whysoserious/ExplodeFragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroidx/fragment/app/FragmentActivity;->finish()V

    .line 39
    return-void
.end method
