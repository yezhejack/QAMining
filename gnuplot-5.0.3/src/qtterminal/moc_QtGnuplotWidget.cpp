/****************************************************************************
** Meta object code from reading C++ file 'QtGnuplotWidget.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "QtGnuplotWidget.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'QtGnuplotWidget.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_QtGnuplotWidget[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       8,   14, // methods
       5,   54, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: signature, parameters, type, tag, flags
      16,   27,   27,   27, 0x05,
      28,   55,   27,   27, 0x05,

 // slots: signature, parameters, type, tag, flags
      62,   27,   27,   27, 0x0a,
      80,   97,   27,   27, 0x0a,
     105,  126,   27,   27, 0x0a,
     135,   27,   27,   27, 0x0a,
     149,  126,   27,   27, 0x0a,
     172,  126,   27,   27, 0x0a,

 // properties: name, type, flags
     193,  203, 0x01095103,
     208,  203, 0x01095103,
     216,  203, 0x01095103,
     231,  247, 0x43095103,
     254,  203, 0x01095103,

       0        // eod
};

static const char qt_meta_stringdata_QtGnuplotWidget[] = {
    "QtGnuplotWidget\0plotDone()\0\0"
    "statusTextChanged(QString)\0status\0"
    "copyToClipboard()\0print(QPrinter&)\0"
    "printer\0exportToPdf(QString)\0fileName\0"
    "exportToEps()\0exportToImage(QString)\0"
    "exportToSvg(QString)\0antialias\0bool\0"
    "rounded\0replotOnResize\0backgroundColor\0"
    "QColor\0statusLabelActive\0"
};

void QtGnuplotWidget::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        QtGnuplotWidget *_t = static_cast<QtGnuplotWidget *>(_o);
        switch (_id) {
        case 0: _t->plotDone(); break;
        case 1: _t->statusTextChanged((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 2: _t->copyToClipboard(); break;
        case 3: _t->print((*reinterpret_cast< QPrinter(*)>(_a[1]))); break;
        case 4: _t->exportToPdf((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 5: _t->exportToEps(); break;
        case 6: _t->exportToImage((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 7: _t->exportToSvg((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData QtGnuplotWidget::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject QtGnuplotWidget::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_QtGnuplotWidget,
      qt_meta_data_QtGnuplotWidget, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &QtGnuplotWidget::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *QtGnuplotWidget::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *QtGnuplotWidget::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_QtGnuplotWidget))
        return static_cast<void*>(const_cast< QtGnuplotWidget*>(this));
    if (!strcmp(_clname, "QtGnuplotEventReceiver"))
        return static_cast< QtGnuplotEventReceiver*>(const_cast< QtGnuplotWidget*>(this));
    return QWidget::qt_metacast(_clname);
}

int QtGnuplotWidget::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 8)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 8;
    }
#ifndef QT_NO_PROPERTIES
      else if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast< bool*>(_v) = antialias(); break;
        case 1: *reinterpret_cast< bool*>(_v) = rounded(); break;
        case 2: *reinterpret_cast< bool*>(_v) = replotOnResize(); break;
        case 3: *reinterpret_cast< QColor*>(_v) = backgroundColor(); break;
        case 4: *reinterpret_cast< bool*>(_v) = statusLabelActive(); break;
        }
        _id -= 5;
    } else if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: setAntialias(*reinterpret_cast< bool*>(_v)); break;
        case 1: setRounded(*reinterpret_cast< bool*>(_v)); break;
        case 2: setReplotOnResize(*reinterpret_cast< bool*>(_v)); break;
        case 3: setBackgroundColor(*reinterpret_cast< QColor*>(_v)); break;
        case 4: setStatusLabelActive(*reinterpret_cast< bool*>(_v)); break;
        }
        _id -= 5;
    } else if (_c == QMetaObject::ResetProperty) {
        _id -= 5;
    } else if (_c == QMetaObject::QueryPropertyDesignable) {
        _id -= 5;
    } else if (_c == QMetaObject::QueryPropertyScriptable) {
        _id -= 5;
    } else if (_c == QMetaObject::QueryPropertyStored) {
        _id -= 5;
    } else if (_c == QMetaObject::QueryPropertyEditable) {
        _id -= 5;
    } else if (_c == QMetaObject::QueryPropertyUser) {
        _id -= 5;
    }
#endif // QT_NO_PROPERTIES
    return _id;
}

// SIGNAL 0
void QtGnuplotWidget::plotDone()
{
    QMetaObject::activate(this, &staticMetaObject, 0, 0);
}

// SIGNAL 1
void QtGnuplotWidget::statusTextChanged(const QString & _t1)
{
    void *_a[] = { 0, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}
QT_END_MOC_NAMESPACE
