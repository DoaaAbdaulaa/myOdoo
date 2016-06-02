import base64
from tempfile import TemporaryFile

from openerp import models,fields,api

class odooHrInhired(models.Model):

    _inherit ="hr.attendance"
    image=fields.Binary()

    @api.onchange('employee_id','image')
    @api.model
    def create(self, values):
        contacts1 = self.env['hr.employee'].search([('id','=',values['employee_id'])])
        values['image']=contacts1.image
        return super(odooHrInhired,self).create(values)

    @api.onchange('employee_id')
    def _onchange_nameEmployee(self):
         return {
            'warning': {
                'title': "Something bad happened",
                'message': "It was very bad indeed",
            }
        }



class odooHrEmployeeInherit(models.Model):
    _inherit ="hr.employee"
    #upload file for  new employee
    data= fields.Binary('File')
    #imagesd= fields.Many2one(comodel_name="ir.attachment", string="Images")


    # def import_file(self, cr, uid, ids, context=None):
    #     fileobj = TemporaryFile('w+')
    #     fileobj.write(base64.decodestring('data'))
    #     return
