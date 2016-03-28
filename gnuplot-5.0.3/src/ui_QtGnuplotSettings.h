/********************************************************************************
** Form generated from reading UI file 'QtGnuplotSettings.ui'
**
** Created by: Qt User Interface Compiler version 4.8.7
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_QTGNUPLOTSETTINGS_H
#define UI_QTGNUPLOTSETTINGS_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QComboBox>
#include <QtGui/QDialog>
#include <QtGui/QDialogButtonBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_settingsDialog
{
public:
    QVBoxLayout *verticalLayout_2;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QPushButton *backgroundButton;
    QSpacerItem *horizontalSpacer;
    QLabel *sampleColorLabel;
    QCheckBox *antialiasCheckBox;
    QCheckBox *replotOnResizeCheckBox;
    QCheckBox *roundedCheckBox;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label;
    QComboBox *mouseLabelComboBox;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *settingsDialog)
    {
        if (settingsDialog->objectName().isEmpty())
            settingsDialog->setObjectName(QString::fromUtf8("settingsDialog"));
        settingsDialog->resize(269, 186);
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/images/settings"), QSize(), QIcon::Normal, QIcon::Off);
        settingsDialog->setWindowIcon(icon);
        verticalLayout_2 = new QVBoxLayout(settingsDialog);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        backgroundButton = new QPushButton(settingsDialog);
        backgroundButton->setObjectName(QString::fromUtf8("backgroundButton"));

        horizontalLayout->addWidget(backgroundButton);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        sampleColorLabel = new QLabel(settingsDialog);
        sampleColorLabel->setObjectName(QString::fromUtf8("sampleColorLabel"));

        horizontalLayout->addWidget(sampleColorLabel);


        verticalLayout->addLayout(horizontalLayout);

        antialiasCheckBox = new QCheckBox(settingsDialog);
        antialiasCheckBox->setObjectName(QString::fromUtf8("antialiasCheckBox"));

        verticalLayout->addWidget(antialiasCheckBox);

        replotOnResizeCheckBox = new QCheckBox(settingsDialog);
        replotOnResizeCheckBox->setObjectName(QString::fromUtf8("replotOnResizeCheckBox"));

        verticalLayout->addWidget(replotOnResizeCheckBox);

        roundedCheckBox = new QCheckBox(settingsDialog);
        roundedCheckBox->setObjectName(QString::fromUtf8("roundedCheckBox"));

        verticalLayout->addWidget(roundedCheckBox);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        label = new QLabel(settingsDialog);
        label->setObjectName(QString::fromUtf8("label"));
        label->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        horizontalLayout_2->addWidget(label);

        mouseLabelComboBox = new QComboBox(settingsDialog);
        mouseLabelComboBox->setObjectName(QString::fromUtf8("mouseLabelComboBox"));

        horizontalLayout_2->addWidget(mouseLabelComboBox);


        verticalLayout->addLayout(horizontalLayout_2);


        verticalLayout_2->addLayout(verticalLayout);

        buttonBox = new QDialogButtonBox(settingsDialog);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout_2->addWidget(buttonBox);


        retranslateUi(settingsDialog);
        QObject::connect(buttonBox, SIGNAL(accepted()), settingsDialog, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), settingsDialog, SLOT(reject()));

        QMetaObject::connectSlotsByName(settingsDialog);
    } // setupUi

    void retranslateUi(QDialog *settingsDialog)
    {
        settingsDialog->setWindowTitle(QApplication::translate("settingsDialog", "Terminal configuration", 0, QApplication::UnicodeUTF8));
        backgroundButton->setText(QApplication::translate("settingsDialog", "Select background color", 0, QApplication::UnicodeUTF8));
        sampleColorLabel->setText(QApplication::translate("settingsDialog", "Sample", 0, QApplication::UnicodeUTF8));
        antialiasCheckBox->setText(QApplication::translate("settingsDialog", "Antialias", 0, QApplication::UnicodeUTF8));
        replotOnResizeCheckBox->setText(QApplication::translate("settingsDialog", "Replot on resize", 0, QApplication::UnicodeUTF8));
        roundedCheckBox->setText(QApplication::translate("settingsDialog", "Rounded line ends", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("settingsDialog", "Mouse label", 0, QApplication::UnicodeUTF8));
        mouseLabelComboBox->clear();
        mouseLabelComboBox->insertItems(0, QStringList()
         << QApplication::translate("settingsDialog", "Status bar", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("settingsDialog", "Tool bar", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("settingsDialog", "Above plot", 0, QApplication::UnicodeUTF8)
         << QApplication::translate("settingsDialog", "None", 0, QApplication::UnicodeUTF8)
        );
    } // retranslateUi

};

namespace Ui {
    class settingsDialog: public Ui_settingsDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QTGNUPLOTSETTINGS_H
