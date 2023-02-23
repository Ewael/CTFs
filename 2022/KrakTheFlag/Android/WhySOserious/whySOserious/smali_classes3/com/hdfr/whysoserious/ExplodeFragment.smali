.class public Lcom/hdfr/whysoserious/ExplodeFragment;
.super Landroidx/fragment/app/Fragment;
.source "ExplodeFragment.java"


# instance fields
.field btn:Landroid/widget/Button;

.field private mViewModel:Lcom/hdfr/whysoserious/ExplodeViewModel;


# direct methods
.method public constructor <init>()V
    .locals 0

    .line 13
    invoke-direct {p0}, Landroidx/fragment/app/Fragment;-><init>()V

    return-void
.end method

.method public static newInstance()Lcom/hdfr/whysoserious/ExplodeFragment;
    .locals 1

    .line 16
    new-instance v0, Lcom/hdfr/whysoserious/ExplodeFragment;

    invoke-direct {v0}, Lcom/hdfr/whysoserious/ExplodeFragment;-><init>()V

    return-object v0
.end method


# virtual methods
.method public onCreateView(Landroid/view/LayoutInflater;Landroid/view/ViewGroup;Landroid/os/Bundle;)Landroid/view/View;
    .locals 2
    .param p1, "inflater"    # Landroid/view/LayoutInflater;
    .param p2, "container"    # Landroid/view/ViewGroup;
    .param p3, "savedInstanceState"    # Landroid/os/Bundle;

    .line 26
    invoke-virtual {p0}, Lcom/hdfr/whysoserious/ExplodeFragment;->getView()Landroid/view/View;

    move-result-object v0

    const v1, 0x7f08015f

    invoke-virtual {v0, v1}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/Button;

    iput-object v0, p0, Lcom/hdfr/whysoserious/ExplodeFragment;->btn:Landroid/widget/Button;

    .line 28
    const v0, 0x7f0b0030

    const/4 v1, 0x0

    invoke-virtual {p1, v0, p2, v1}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;Z)Landroid/view/View;

    move-result-object v0

    return-object v0
.end method

.method public onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V
    .locals 2
    .param p1, "view"    # Landroid/view/View;
    .param p2, "savedInstanceState"    # Landroid/os/Bundle;

    .line 33
    invoke-super {p0, p1, p2}, Landroidx/fragment/app/Fragment;->onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V

    .line 34
    const v0, 0x7f08015f

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/Button;

    iput-object v0, p0, Lcom/hdfr/whysoserious/ExplodeFragment;->btn:Landroid/widget/Button;

    .line 35
    new-instance v1, Lcom/hdfr/whysoserious/ExplodeFragment$1;

    invoke-direct {v1, p0}, Lcom/hdfr/whysoserious/ExplodeFragment$1;-><init>(Lcom/hdfr/whysoserious/ExplodeFragment;)V

    invoke-virtual {v0, v1}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    .line 41
    return-void
.end method
